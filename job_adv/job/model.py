from ..app import app, db


class Job(db.Model):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(64000))
    owner_account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    def __init__(self, title, description, owner_account_id):
        self.title = title
        self.description = description
        self.owner_account_id = owner_account_id

    def create(self):
        db.session.add(self)
        db.session.commit()

