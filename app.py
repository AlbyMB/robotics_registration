import os
from flask import Flask,render_template,request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)

class User( db.Model):
    id = db.Column(db.Integer, primary_key=True)
    submissionDate = db.Column(db.Date,nullable=False)
    studentFirstName = db.Column(db.String(80),nullable=False)
    studentMiddleName = db.Column(db.String(80),nullable=False)
    studentLastName = db.Column(db.String(80),nullable=False)
    dateOfBirth = db.Column(db.Date,nullable=False)
    gender = db.Column(db.String(80),nullable=False)
    phoneNumber = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(80),nullable=False)
    schoolName = db.Column(db.String(80),nullable=False)
    grade = db.Column(db.String(80),nullable=False)
    parentFirstName = db.Column(db.String(80),nullable=False)
    parentMiddleName = db.Column(db.String(80))
    parentLastName = db.Column(db.String(80))
    street = db.Column(db.String(80),nullable=False)
    city = db.Column(db.String(80),nullable=False)
    postalCode = db.Column(db.String(80),nullable=False)
    secondPhone = db.Column(db.String(80),nullable=False)
    remarks = db.Column(db.String(80))

table_created = False

@app.before_request
def create_tables():
    global table_created
    if not table_created:
        db.create_all()
        table_created = True

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods =['POST'])
def submit():
    submissionDate = datetime.today().date()
    studentFirstName = request.form.get('studentFirstName')
    studentMiddleName = request.form['studentMiddleName']
    studentLastName = request.form['studentLastName']
    dateOfBirth = request.form['dateOfBirth']
    gender = request.form['gender']
    phoneNumber = request.form['phoneNumber']
    email = request.form['email']
    schoolName = request.form['schoolName']
    grade = request.form['grade']
    parentFirstName = request.form['parentFirstName']
    parentMiddleName = request.form['parentMiddleName']
    parentLastName = request.form['parentLastName']
    street = request.form['street']
    city = request.form['city']
    postalCode = request.form['postalCode']
    secondPhone = request.form['secondPhone']
    remarks = request.form['remarks']

    new_user = User(submissionDate=submissionDate, studentFirstName=studentFirstName,
                    studentMiddleName=studentMiddleName, studentLastName=studentLastName
                    , dateOfBirth=dateOfBirth, gender=gender,phoneNumber=phoneNumber,
                    email=email,schoolName=schoolName,grade=grade,parentFirstName=parentFirstName
                    ,parentMiddleName=parentMiddleName,parentLastName=parentLastName,
                    street=street,city=city,postalCode=postalCode,secondPhone=secondPhone,remarks=remarks)

    db.session.add(new_user)
    db.session.commit()
    
    print( f""",{studentFirstName} {studentMiddleName} {studentLastName} {
dateOfBirth} {gender} {phoneNumber} {email} {schoolName} {grade}
{parentFirstName} {parentMiddleName} {parentLastName} {street}, {city}, {postalCode}
{secondPhone} {remarks}""")

    return f""",{studentFirstName} {studentMiddleName} {studentLastName} {
dateOfBirth} {gender} {phoneNumber} {email} {schoolName} {grade}
{parentFirstName} {parentMiddleName} {parentLastName} {street}, {city}, {postalCode}
{secondPhone} {remarks}"""
    
if __name__=='__main__':
    app.run(debug=True)
