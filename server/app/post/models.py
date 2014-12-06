from mongoengine import *


class user_model(Document):
	firstname=StringField(max_length=300,required=True)
	lastname=StringField(max_length=300,required=True)
	username=StringField(max_length=100,required=True)
	email=StringField(required=True)
	password=StringField(required=True)


	 


class post_model(Document):
	title=StringField(max_length=120,required=True)
	author=ReferenceField(user_model,reverse_delete_rule=CASCADE)
	location=GeoPointField()	
	#tags=ListField(StringField(max_length=30))
	#comments=ListField(EmbeddedDocumentField(Comment))
	meta={'allow_inheritance':True}


class TextPost(post_model):
	content=StringField()

class ImagePost(post_model):
	image_path=StringField()

class LinkPost(post_model):
	link_url=StringField()

class Comment(EmbeddedDocument):
	content=StringField()
	name=StringField(max_length=120)