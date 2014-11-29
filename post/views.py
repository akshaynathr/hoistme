from flask import Blueprint
from flask.ext import restful

posts=Blueprint('posts',__name__,template_folder='templates',static_folder='static')
api=restful.Api(posts)

class POST(restful.Resource):
	def get(self):
		return "Welcome"
	
	def put(self):
		return "Received"



api.add_resource(POST,'/post')
