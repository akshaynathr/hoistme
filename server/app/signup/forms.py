from flask_wtf import Form
from wtforms import TextField,PasswordField,validators,BooleanField
WTF_CSRF_ENABLED = True

class RegistrationForm(Form):
	firstname=TextField('Firstname',[validators.Length( max=25)])
	lastname=TextField('Lastname',[validators.Length( max=25)])

	username=TextField('Username',[validators.Length(min=4,max=25)])
	email=TextField('Email address',[validators.Length(min=6,max=35)])
	password=PasswordField('Password',[validators.Required(),validators.EqualTo('confirm',message="Passwords must match")])
	confirm=PasswordField('Repeat Password')
	accept_tos=BooleanField('Accept the TOS',[validators.Required()])