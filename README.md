# job_adv

## Installation
* This app is using ```Postgres``` database & ```Python3```, so you will need to install them first.
* Create database named job_adv.
* Install dependencies ```pip install -r requirements.txt```
* Set environment variables:<br>
  ```SQLALCHEMY_DATABASE_URI='postgresql://username:password@localhost:5432/job_adv'```<br>
  ```SECRET_KEY='MY-SECRET-KEY'```<br>
  ```UPLOAD_FOLDER='/MY-DATA-FOLDER-PATH'```<br>
  ```MAX_CONTENT_PATH=10000```<br>
* Run database migrations: <br>
  ```flask db init``` <br>
  ```flask db migrate```<br>
  ```flask db upgrade```<br>
 * Run the app:<br>
 ```flask run```
 
 ## Features:
 * Signup page with frontend fields validations.
 * Upload documents to local storage instead of binaries in database.
 * Creating new Jobs if user is logged in only.
 * Viewing Jobs for public and private users.
 * Sign up with Google accounts.
 
 ## Future work:
 * Implement the ability to apply for posted jobs.
 * Implement different types of accounts "Admin, Employer, Employee, ...etc"
 * Improve User interface.
