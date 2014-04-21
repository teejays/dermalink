from app import app, db, lm, bcrypt, mail
from flask import render_template, flash, redirect, session, url_for, request, g, jsonify
from flask.ext.login import login_user, logout_user, current_user, login_required
from flaskext.uploads import UploadSet, configure_uploads, IMAGES
from models import User, Image, Issue, Patient, Doctor, Diagnosis
from datetime import datetime
from werkzeug import secure_filename
from twilio.rest import TwilioRestClient
# Forms
from forms import LoginForm, SignupForm, CreateIssueForm, DermSignupForm, EditProfileForm, DiagnosisForm
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, FileField, TextAreaField, SelectField, HiddenField, RadioField, validators
from wtforms.validators import *
from wtforms.ext.sqlalchemy.orm import model_form

#from flask.ext.sendmail import Message
from flask.ext.mail import Message

 
# Twilio Account Information
# account = 'AC6056ccab9b128c038c932d4bbf81b662'
# token = 'd6a72dff4e0f118e2e52d15ef51f4548'
# client = TwilioRestClient(account, token)
# MY_TWILIO_NUMBER = '+14408478798'

reserved_usernames = 'home signup login logout post'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

def SendSMS(number, body):
	return 1
	# client.sms.messages.create(to='+14403343014', from_=MY_TWILIO_NUMBER,
 #                                     body=body)

def sendEmail(body):
	msg = Message('Test',
                  sender='talhajansari@gmail.com',
                  recipients=["talhajansari+test@gmail.com"])
	msg.body = "Test: Body of message"
	mail.send(msg)

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))


@app.before_request   
def before_request():
	g.user = current_user

# def isPatientComplete(patient):
# 	if patient.firstName is not None:
# 		if patient.lastName is not None:
# 			if patient.age !='0':
# 				if patient.phone !='0':
# 					if patient.gender == 'male' or patient.gender == 'female':
# 						patient.isComplete = 1
# 						db.session.commit()
# 						return 1
# 	return 0

# def isDoctorComplete(doctor):
# 	if doctor.firstName is not None and doctor.lastName is not None and doctor.hospital is not None and doctor.city is not None and doctor.state is not None and doctor.country is not None and doctor.issueLimit != '0' and doctor.phone !='0':
# 		doctor.isComplete = 1
# 		db.session.commit()
# 		return 1
# 	return 0

@app.route('/')
@app.route('/index')
def index():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for("home"))
	else:
		loginForm = LoginForm()
		signupForm = SignupForm()
		derm_signupForm = DermSignupForm()
		return render_template("index.html", title = 'Log in', form1=loginForm, form2=signupForm, form3=derm_signupForm)


@app.route("/login", methods=["POST"])
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('home'))
	loginForm = LoginForm()
	signupForm = SignupForm()
	derm_signupForm = DermSignupForm()
	if loginForm.validate_on_submit():
		email = loginForm.email.data
		password = loginForm.password.data
		if email is None or password is None:
			flash('Invalid login. Please try again.')
			return redirect(url_for('index'))
		user = User.query.filter_by(email = email).first()
		if user is None:
			flash('This email does not exist. Please try again.')
			return redirect(url_for('index'))
		if user is not None:
			if bcrypt.check_password_hash(user.password, password) is False:
				flash('Invalid password. Please try again.')
				return redirect(url_for('index'))
			login_user(user, remember=True)
			flash('Succesfully logged in.')	
			return redirect(url_for("home"))
	return render_template("index.html", title = 'Sign In', form1=loginForm, form2=signupForm, form3=derm_signupForm)


@app.route("/signup", methods=["POST"])
def signup():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('home'))
	loginForm = LoginForm()
	signupForm = SignupForm()
	derm_signupForm = DermSignupForm()
	if signupForm.validate_on_submit():
		email = signupForm.email.data
		if email not in reserved_usernames.split():
			password = signupForm.password.data
			password_hash = bcrypt.generate_password_hash(password)
			user = User.query.filter_by(email = email).first() # Check if that email already exists
			#if dermatologist is not None or user is not None:
			if user is not None:
				flash('That email is already in use')
				return redirect(url_for('index'))			
			# Create the user
			user = User(password=password_hash, email=email, role='PATIENT')
			db.session.add(user)
			db.session.flush()
			patient = Patient(user_id=user.id, isComplete = 0)
			db.session.add(patient)
			db.session.flush()
			user.patient = patient
			db.session.flush()
			db.session.commit()
		login_user(user, remember=True)
		sendEmail('You have signed up!')
		#return redirect(request.args.get("next") or url_for("editProfile", username=user.username, user=user))
		return redirect(url_for("editProfile", id=user.id))
	return render_template("index.html", title = 'Sign Up', form1=loginForm, form2=signupForm, form3=derm_signupForm)


@app.route("/derm_signup", methods=["POST"])
def derm_signup():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('issues'))
	loginForm = LoginForm()
	signupForm = SignupForm()
	derm_signupForm = DermSignupForm()
	if derm_signupForm.validate_on_submit():
		email = derm_signupForm.email.data
		if email not in reserved_usernames.split():
			password = derm_signupForm.password.data
			password_hash = bcrypt.generate_password_hash(password)
			user = User.query.filter_by(email = email).first() # Check if that email already exists
			if user is not None:
				flash('That email is already in use')
				return redirect(url_for('index'))
			# Create the user
			user = User(password=password_hash, email=email, role='DOCTOR')
			db.session.add(user)
			db.session.flush()
			doctor = Doctor(user_id=user.id, isComplete = 0)
			db.session.add(doctor)
			db.session.flush()
			user.doctor = doctor
			db.session.flush()
			db.session.commit()
		login_user(user, remember=True)
		#return redirect(request.args.get("next") or url_for("editProfile", username=user.username, user=user))
		return redirect(url_for("editProfile", id=user.id))
	return render_template("index.html", title = 'Sign Up', form1=loginForm, form2=signupForm, form3=derm_signupForm)


@app.route('/home')
@login_required
def home():
	createIssueForm = CreateIssueForm()
	if g.user.isPatient(): #is not doctor
		issues = Issue.query.filter_by(patient_id=g.user.patient.id) 
		complete = g.user.patient.isComplete()
		return render_template('home.html', issues=issues, isDoctor=0, isComplete=complete, form1=createIssueForm)
	elif g.user.isDoctor():
		doctor_id = g.user.doctor.id
		is_complete = g.user.doctor.isComplete()
		issues = Issue.query.filter(Issue.doctors.any(id=doctor_id)).all()
		return render_template('home.html', issues=issues, isDoctor=1)



@app.route("/edit/<id>", methods=["POST", "GET"])
@login_required
def editProfile(id):
	user = User.query.get(id)
	if user == None:
		return redirect(url_for('home'))
	if g.user.id is not int(id):
		return redirect(url_for('home'))
	if g.user.isPatient():
		MyForm = model_form(Patient, Form, exclude=['issues', 'user', 'is_complete'])
		patient = g.user.patient
		form = MyForm(request.form, patient)
	if g.user.isDoctor():
		MyForm = model_form(Doctor, Form, exclude=['issues', 'diagnoses', 'user', 'is_complete', 'is_available','is_certified', 'rating'])
		#MyForm.gender = RadioField(choices=[('male', 'male'), ('female', 'female')])
		MyForm.issue_limit = SelectField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])
		doctor = g.user.doctor
		form = MyForm(request.form, doctor)
		
	if request.method == 'POST':
		if g.user.isPatient() and form.validate_on_submit(): #is not doctor
			form.populate_obj(patient)
			# if form.firstName.data:
			# 	patient.firstName = form.firstName.data
			# if form.lastName.data:
			# 	patient.lastName = form.lastName.data
			# if form.gender.data:
			# 	patient.gender = form.gender.data
			# if form.phone.data:
			# 	patient.phone = form.phone.data
			# if form.age.data:
			# 	patient.age = int(form.age.data)
			# if form.ethnicity.data:
			# 	patient.ethnicity = form.ethnicity.data
			# if form.password.data:
			# 	if form.confirmPassword.data is None:
			# 		flash('Please confirm your password.')
			# 		return redirect(url_for("editProfile", id=user.id))
			# 	if form.password.data != form.confirmPassword.data:
			# 		flash('Confirmation does not match.')
			# 		return redirect(url_for("editProfile", id=user.id))
			# 	password_hash = bcrypt.generate_password_hash(form.password.data)
			# 	user.password = password_hash
			db.session.commit()
			return redirect(url_for('home'))
		elif g.user.isDoctor():
			#form = model_form(Doctor, exclude=['issues', 'diagnoses', 'user', 'is_complete', 'is_available','is_certified', 'rating'])(request.form)
			form.populate_obj(doctor)
			# if form.lastName.data:
			# 	doctor.lastName = form.lastName.data
			# if form.hospital.data:
			# 	doctor.hospital = form.hospital.data
			# if form.city.data:
			# 	doctor.city = form.city.data
			# if form.state.data:
			# 	doctor.state = form.state.data
			# if form.country.data:
			# 	doctor.country = form.country.data
			# if form.phone.data:
			# 	doctor.phone = form.phone.data
			# if form.password.data:
			# 	if form.confirmPassword.data is None:
			# 		flash('Please confirm your password.')
			# 		return redirect(url_for("editProfile", id=user.id))
			# 	if form.password.data != form.confirmPassword.data:
			# 		flash('Confirmation does not match.')
			# 		return redirect(url_for("editProfile", id=user.id))
			# 	password_hash = bcrypt.generate_password_hash(form.password.data)
			# 	user.password = password_hash
			db.session.commit()
			doctor.isComplete()
			return redirect(url_for('home'))
	# elif request.method == 'GET':
	#form = EditProfileForm(obj=user)
	return render_template("test.html", form=form)
	return render_template("edit_profile.html", form=myForm)


@app.route('/create', methods=['GET', 'POST'])
@login_required
def create_issue():
	createIssueForm = CreateIssueForm()
	if request.method=='GET':
		return render_template('create_issue.html', form=createIssueForm)	
	if createIssueForm.validate_on_submit():
		summary = createIssueForm.summary.data
		filename = secure_filename(createIssueForm.image.data.filename)
		user_id = g.user.id
		patient_id = g.user.patient.id
		issue = Issue(summary=summary, timestamp= datetime.utcnow(), patient_id=patient_id, isClosed=0)
		db.session.add(issue)
		db.session.flush()
		image = Image(filename=filename, timestamp= datetime.utcnow(), issue_id=issue.id)
		createIssueForm.image.file.save('uploads/'+str(filename))
		db.session.add(image)
		db.session.flush()
		assignIssueToDoctor(issue)
		db.session.commit()
		issue_id = issue.id
		return redirect(url_for('show_issue', id=issue_id))


@app.route('/home/<id>', methods=['GET', 'POST'])
@login_required
def show_issue(id):
	form = DiagnosisForm()
	if request.method == 'POST': # Diagnose
		issue = Issue.query.get(id)
		summary = form.diagnosis.data
		diagnosis = Diagnosis(diagnosis=summary, doc_id=g.user.doctor.id, issue_id=id, timestamp= datetime.utcnow())
		db.session.add(diagnosis)
		issue.diagnoses.append(diagnosis)
		g.user.doctor.diagnoses.append(diagnosis)
		issue.isClosed = int(form.resolved.data)
		#return form.resolved.data
		db.session.commit()
		#send a message
		SendSMS(issue.patient.phone, "SkinCheck: Your complaint, \'" + str(issue.summary) + "\', has been diagnosed by Dr. " + str(diagnosis.doctor.lastName) + ".")
		#msg = Message("Your complaint, \'" + str(issue.summary) + "\', has been diagnosed by Dr. " + str(diagnosis.doctor.lastName) + ".",
        #          sender="talhajansari+dermalink_sender@gmail.com",
        #          recipients=["talhajansari+dermalink_receiver@gmail.com"])
		return redirect(url_for("show_issue", id=id))
	# else if request.method = GET:
	issue = Issue.query.get(id)
	if g.user.isPatient():
		authenticate = g.user.patient.owns_issue(id)
	elif g.user.isDoctor():
		authenticate = g.user.doctor.owns_issue(id)
	if authenticate is False:
		return redirect(url_for("home"))
	if issue is None: # will never reach this condition - can delete it
		return 'No such issue found'
	pics = Image.query.filter_by(issue_id=id).all()
	URLs = []
	for image in pics:
		url = images.url(image.filename)
		URLs.append(url)
	return render_template('show_issue.html', issue=issue, URLs=URLs, images=images, form=form)


@app.route('/home/<issue_id>/upload', methods=['GET', 'POST'])
@login_required
def upload(issue_id):
	if request.method == 'POST' and 'image' in request.files:
		filename = images.save(request.files['image'])
		image = Image(filename=filename, issue_id=issue_id)
		db.session.add(image)
		db.session.commit()
		return redirect(url_for("show_issue", id=issue_id))
	issue = Issue.query.get(issue_id)
	#return str(issue.summary)
	return render_template('upload.html', issue=issue)


@app.route("/logout")
@login_required
def logout():
	logout_user()
	flash('Succesfully logged out.')
	form = LoginForm()
	return redirect("/")


## Other functions

# For now, it only assigns the issues to the first dermatologist
def assignIssueToDoctor(issue):
	doctors = Doctor.query.filter_by(isAvailable=1, isComplete=1).all()
	if len(doctors) is 0: # No available doctors
		doc = Doctor.query.first()
		doc.issues.append(issue)
		db.session.commit()
		return doc
	else: # At least one doctor available
		for doc in doctors:
			if doc.isAvailableMethod():
				doc.issues.append(issue)
				doc.isAvailableMethod()
				db.session.commit()
				# Send SMS notification
				SendSMS(doc.phone, "SkinCheck: You have been assigned a new issue to diagnose")
				return doc




