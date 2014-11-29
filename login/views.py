from flask import Blueprint,render_template
from flask_wtf import Form
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'


signUp=Blueprint("signUp",__name__, template_folder="templates",static_folder="static")

class MyForm(Form):
	username=StringField('name',validators=[DataRequired()])
	password=PasswordField('password',validators=[DataRequired()])


@signUp.route('/signup',methods=['GET','POST'])
def signUP():
	form=MyForm(csrf_enabled=False)
	if form.validate_on_submit():
		return "Recieved Data"+form.username.data
	return render_template('login.html',form=form) 

