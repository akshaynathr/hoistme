from flask import Blueprint,render_template,request,redirect,url_for,flash
from app.post.models import user_model

from forms import RegistrationForm


signup_blueprint=Blueprint("signup_blueprint",__name__,template_folder='templates',static_folder='static')
	
@signup_blueprint.route('/signup',methods=['GET','POST'])
def signup():
	print("form.validate")
	form=RegistrationForm(request.form)
	print(form.validate())
	if  form.validate_on_submit() and check_duplicates(form.email.data):
		
		print("saved")
		user=user_model(form.firstname.data,form.lastname.data,form.username.data,form.email.data,form.password.data)
		user.save()
	elif request.method=='POST':
		flash("User Already exist")
		return render_template('signup.html',form=form)
	return render_template('signup.html',form=form)



@signup_blueprint.route('/error',methods=['GET'])
def error():
	return render_template('error.html')


def check_duplicates(emailid):
	user=user_model.objects(email=emailid)[0]
	print('duplicates checking'+ user.firstname)
	if user is None:
		print('None')
		return True
	else:
		print('already exist')
		return False
 
