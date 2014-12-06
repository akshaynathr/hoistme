from app.server import app
from flask import render_template,request,g,session
from flask.ext.login import LoginManager,login_user,logout_user,current_user,login_required
from app.post.models import user_model
lm=LoginManager(app)
lm.login_view='login'


@lm.user_loader
def load_user(id):
	print(user_model.objects(id=(id)))
	return user_model.objects(id=(id))

@app.before_request
def before_request():
    g.user = current_user
 
@app.route('/login',methods=['GET','POST'])
def login():
	 print("readched")
	 if request.method=='GET':
	 	return render_template('lgin.html')
	 username=request.form['username']
	 password=request.form['password']
	 print("readched")
	 try:
	 	registered_user=user_model.objects(username=username)[0]
	 	print(registered_user.firstname)
	 except:
	 	return "No user"
	 if registered_user is None:
	 	return "Invalid password or username"
	 login_user(registered_user)

	 return render_template('hi.html')

@app.route('/logout')
def logout():
	logout_user()
	return render_template('login.html')


@app.route('/hi')
@login_required
def hi():
	return render_template('hi.html')

