#from flask.ext.mongoengine.fields import *
from app.server import db

class post_model(db.Document):
	title=db.StringField(max_length=120)
	author=db.StringField()
	content=db.StringField(max_length=200)
	


