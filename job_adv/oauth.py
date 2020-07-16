from .app import app
from .account.model import Account

import json
from os import environ

from rauth import OAuth1Service, OAuth2Service
from flask import current_app, url_for, request, redirect, session, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user,\
    current_user

app.config['OAUTH_CREDENTIALS'] = {
    'google': {
        'id': environ.get('GOOGLE_CLIENT_ID'),
        'secret': environ.get('GOOGLE_SECRET')
    }
}


class OAuthSignIn(object):
    providers = None

    def __init__(self, provider_name):
        self.provider_name = provider_name
        credentials = current_app.config['OAUTH_CREDENTIALS'][provider_name]
        self.consumer_id = credentials['id']
        self.consumer_secret = credentials['secret']

    def authorize(self):
        pass

    def callback(self):
        pass

    def get_callback_url(self):
        return url_for('oauth_callback', provider=self.provider_name,
                       _external=True)

    @classmethod
    def get_provider(self, provider_name):
        if self.providers is None:
            self.providers = {}
            for provider_class in self.__subclasses__():
                provider = provider_class()
                self.providers[provider.provider_name] = provider
        return self.providers[provider_name]


class GoogleSignIn(OAuthSignIn):
    def __init__(self):
        super(GoogleSignIn, self).__init__('google')
        self.service = OAuth2Service(
            name='google',
            client_id=self.consumer_id,
            client_secret=self.consumer_secret,
            authorize_url='https://accounts.google.com/o/oauth2/auth',
            access_token_url='https://oauth2.googleapis.com/token',
            base_url='https://www.googleapis.com/'
        )

    def authorize(self):
        return redirect(self.service.get_authorize_url(
            scope='email',
            response_type='code',
            redirect_uri=self.get_callback_url())
        )

    def callback(self):
        def decode_json(payload):
            return json.loads(payload.decode('utf-8'))

        if 'code' not in request.args:
            return None, None, None
        oauth_session = self.service.get_auth_session(
            data={'code': request.args['code'],
                  'grant_type': 'authorization_code',
                  'redirect_uri': self.get_callback_url()},
            decoder=decode_json
        )
        me = oauth_session.get('oauth2/v2/userinfo').json()
        return (
            'google$' + me['id'],
            me.get('email').split('@')[0],
            me.get('email')
        )


@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('app_entry'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('app_entry'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('app_entry'))
    user = Account.query.filter_by(social_id=social_id).first()
    if not user:
        user = Account(social_id=social_id, user_name=username, email_address=email)
        user.create()
    login_user(user, True)
    return redirect(url_for('app_entry'))
