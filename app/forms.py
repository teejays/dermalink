from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, FileField, TextAreaField, SelectField, HiddenField, RadioField, validators
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import Required, Email
from flask.ext.uploads import UploadSet, IMAGES

images = UploadSet('images', IMAGES)


class LoginForm(Form):
    email = TextField('email', validators = [Required(), Email()])
    password = PasswordField('password', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class SignupForm(Form):
    email = TextField('email', validators = [Required(), Email()])
    password = PasswordField('password', validators = [Required()])

class DermSignupForm(Form):
    email = TextField('email', validators = [Required(), Email()])
    password = PasswordField('password', validators = [Required()])

class ForgotPasswordForm(Form):
    email = TextField('email', validators = [Required(), Email()])

class ChangePasswordForm(Form):
    password = PasswordField('New Password', validators = [validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password', validators = [Required()])

class EditProfileForm(Form):
    password = PasswordField('password')
    confirmPassword = PasswordField('confirmPassword')
    firstName = TextField('firstName', default='as')
    lastName = TextField('lastName')
    gender = RadioField('gender', choices=[('male', 'male'), ('female', 'female')])
    age = TextField('age')
    ethnicity = TextField('ethnicity')
    hospital = TextField('hospital')
    city = TextField('city')
    state = TextField('state')
    country = TextField('country')
    phone = TextField('phone')
    issueLimit = SelectField('issueLimit', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])


class CreateIssueForm(Form):
    summary = TextAreaField('summary', validators = [Required()])
    image = FileField('image', validators = [FileRequired(), FileAllowed(images, 'Images Only!')])
    #image2 = FileField('image2', validators = [FileRequired(), FileAllowed(images, 'Images Only!')])

class UploadImageForm(Form):
    image = FileField('image', validators = [FileRequired(), FileAllowed(images, 'Images Only!')])

class DiagnosisForm(Form):
    diagnosis = TextAreaField('diagnosis', validators = [Required()])
    resolved = SelectField('resolved', choices = [(0, 'No'),(1, 'Yes')], default=1) 


