from flask import Blueprint,render_template,request
from app.post.models import user_model

from forms import RegistrationForm


signup_blueprint=Blueprint("signup_blueprint",__name__,template_folder='templates',static_folder='static')
	
@signup_blueprint.route('/signup',methods=['GET','POST'])
def signup():
	print("form.validate")
	form=RegistrationForm(request.form)
	print(form.validate())
	if  form.validate_on_submit():
		print("saved")
		user=user_model(form.firstname.data,form.lastname.data,form.username.data,form.email.data,form.password.data)
		user.save()

		
		return "Thank You"+user.firstname+" "+user.lastname
	
	 
	return render_template('signup.html',form=form)


 
