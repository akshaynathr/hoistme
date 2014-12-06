from flask import Blueprint,request,jsonify,abort 
import json
from models import post_model,user_model
from flask.ext.restful import Api,Resource
from flask.ext.login import login_required
posts_blueprint=Blueprint('posts_blueprint',__name__,template_folder='templates',static_folder='static')
api=Api(posts_blueprint)


 

class POST(Resource):
	decorators = [login_required]
	def get(self):
		t=[]
		#data=post_model.objects.all()
		try:
			y=user_model.objects(firstname="Rahul")[0]
		except:
			abort(404)
		return "password= " +y.password
	def put(self):
		user=user_model.objects(Q(username=request.form['username']) & Q(password=request.form['password']))
		if user is not None:
		#if request.form['username']=='admin':
			p=post_model() 
			p.title=request.form['title']
			p.author=request.form['author']
			#p.content=request.form['content']
			t=[]
			t.append(float(request.form['lon']))
			t.append(float(request.form['lat']))
			p.location=t
			p.save()
			return request.form['username'] +' saved'
		return "Error in username or password"
	

class Feed(Resource):
	def get(self):
		ta=post_model.objects(author="akshay")[0]
		return ta.title + ' by '+ ta.author+  " - from location"+ str(ta.location)
		
				
		

api.add_resource(POST,'/post')
api.add_resource(Feed,'/feed')


from app.server import app
