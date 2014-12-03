from flask import Blueprint,request,jsonify
import json
from models import post_model,user_model
from flask.ext.restful import Api,Resource
posts_blueprint=Blueprint('posts_blueprint',__name__,template_folder='templates',static_folder='static')
api=Api(posts_blueprint)

 

class POST(Resource):
	def get(self):
		t=[]
		#data=post_model.objects.all()
		y=user_model.objects(firstname="Rahul")[0]
		 
		return "password= " +y.password
	def put(self):
		if request.form['username']=='admin':
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
		ta=post_model.objects(author="aknath332")[0]
		return ta.title + ' by '+ ta.author+  " - from location"+ str(ta.location)
		
				
		

api.add_resource(POST,'/post')
api.add_resource(Feed,'/feed')


from app.server import app
