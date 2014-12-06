from app.server import app
from flask import render_template,request,g,session
from flask.ext.login import LoginManager,login_user,logout_user,current_user,login_required
from app.post.models import user_model
 
 


 


@app.route('/login',methods=['GET','POST'])
def login():
	 print("readched")
	 if request.method=='GET':
	 	return render_template('lgin.html')
	 username=request.form['username']
	 password=request.form['password']
	 try:
	 	registered_user=user_model.objects(username=username)[0]
	 except:
	 
	 	return "Not registered user"
	 
	 if registered_user is not None:
	 	session['email']=registered_user.email

	 	return render_template('hi.html')

@app.route('/logout')
def logout():
	session.pop('email')
	return '''LOGGED OUT'''

@app.route('/hi')
 
def hi():
	if 'email' in session:
		user=user_model.objects(email=session['email'])
		return user[0].firstname
	else:
		return "User not found"
		 
	 

