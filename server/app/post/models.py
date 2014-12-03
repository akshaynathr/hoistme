from mongoengine import *




class post_model(Document):
	title=StringField(max_length=120)
	author=StringField()
	content=StringField(max_length=200)
	location=GeoPointField()	

