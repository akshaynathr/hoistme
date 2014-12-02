from flask import Blueprint,request,jsonify
import json
from models import post_model
from flask.ext.restful import Api,Resource
posts_blueprint=Blueprint('posts_blueprint',__name__,template_folder='templates',static_folder='static')
api=Api(posts_blueprint)

def login(username,password):
	if username != 'admin':
        	return "Error in username or password"



class POST(Resource):
	def get(self):
		t=[]
		data=post_model.objects.all()
		for i in data:
			t.append(i.title)
		return t	
	def put(self):
		if request.form['username']=='admin':
			p=post_model()
			p.title=request.form['title']
			p.author=request.form['author']
			p.content=request.form['content']
			p.save()
			return request.form['username'] +' saved'
		return "Error in username or password"
	

class Feed(Resource):
	def get(self):
		ta=post_model.objects(author="aknath32")[0]
		return ta.title + ' by '+ ta.author
		
				
		

api.add_resource(POST,'/post')
api.add_resource(Feed,'/feed')


from app.server import app
