from app import app, db, lm, bcrypt
from flask import render_template, flash, redirect, session, url_for, request, g, jsonify
from flask.ext.login import login_user, logout_user, current_user, login_required
from flaskext.uploads import UploadSet, configure_uploads, IMAGES
from forms import LoginForm, SignupForm, IssueForm
from models import User, Image, Issue

reserved_usernames = 'home signup login logout post'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)


@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.before_request   
def before_request():
	g.user = current_user


@app.route('/')
@app.route('/index')
def index():
	loginForm = LoginForm()
	signupForm = SignupForm()
	return render_template("index.html", title = 'Log in', form1=loginForm, form2=signupForm)

@app.route("/login", methods=["POST"])
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))
	loginForm = LoginForm()
	signupForm = SignupForm()
	if loginForm.validate_on_submit():
		email = loginForm.email.data
		password = loginForm.password.data
		if email is None or password is None:
			flash('Invalid login. Please try again.')
			return redirect(url_for('index'))
		user = User.query.filter_by(email = email).first()
		if user is None:
			flash('That email does not exist. Please try again.')
			return redirect(url_for('index'))
		if bcrypt.check_password_hash(user.password, password) is False:
			flash('Invalid Login. Please try again.')
			return redirect(url_for('index'))
		login_user(user, remember=True)
		#return redirect(request.args.get("next") or url_for("user", email=user.email, user=user))
		return redirect(url_for("issue"))
	return render_template("index.html", title = 'Sign In', form1=loginForm, form2=signupForm)

@app.route("/signup", methods=["POST"])
def signup():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))
	loginForm = LoginForm
	signupForm = SignupForm()
	if signupForm.validate_on_submit():
		email = signupForm.email.data
		if email not in reserved_usernames.split():
			password = signupForm.password.data
			password_hash = bcrypt.generate_password_hash(password)
			user = User.query.filter_by(email = email).first() # Check if that email already exists
			if user is not None:
				flash('That email is already in use')
				return redirect(url_for('index'))
			
			# Create the user
			user = User(password=password_hash, email=email)
			db.session.add(user)
			db.session.commit()
		login_user(user, remember=True)
		#return redirect(request.args.get("next") or url_for("editProfile", username=user.username, user=user))
		return redirect(url_for("issue"))
	return render_template("index.html", title = 'Sign Up', form1=loginForm, form2=signupForm)


@app.route('/issue')
@login_required
def issue():
	issueForm = IssueForm()
	user = g.user
	issues = Issue.query.filter_by(user_id=user.id) 
	return render_template('issues.html', issues=issues, form1=issueForm)

@app.route('/issue/create', methods=['POST'])
@login_required
def create_issue():
	issueForm = IssueForm()
	if issueForm.validate_on_submit():
		summary = issueForm.summary.data
		user_id = g.user.id
		issue = Issue(summary=summary, user_id=user_id, isClosed=0,)
		db.session.add(issue)
		db.session.commit()
		return redirect(url_for('upload', issue=issue))

# @app.route('/issue/<id>')
# @login_required
# def show_issue(id):
# 	issue = Issue.query.get(id)
# 	if issue is None:
# 		return 'No such issue found'
# 	return render_template('show_issue.html', issue=issue)


@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
	if request.method == 'POST' and 'image' in request.files:
		filename = images.save(request.files['image'])
		issue_id = issue.id
		image = Image(filename=filename, issue_id=issue_id)
		db.session.add(image)
		db.session.commit()
		return redirect(url_for('show_image', id=image.id))
	#issue = Issue.query.get(issue_id)
	return render_template('upload.html', issue=issue)

@app.route('/image/<id>')
@login_required
def show_image(id):
	image = Image.query.get(id)
	if image is None:
		abort(404)
	url = images.url(image.filename)
	return render_template('show_image.html', url=url, image=image)



@app.route("/logout")
@login_required
def logout():
	logout_user()
	form = LoginForm()
	return redirect("/")


