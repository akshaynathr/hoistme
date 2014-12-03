import os

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from mongoengine import connect

connect('hoistme')


basedir=os.path.join(os.path.abspath(os.path.dirname(__file__)),'../')

app=Flask(__name__)
app.config.from_object('app.config')

#flask-mongoengine
app.config["MONGODB_SETTINGS"]={'db':'hoistme'}

#db=MongoEngine(app)

#flask-blueprints
def blueprints():
	from post.views import posts_blueprint
	from signup.views import signup_blueprint
	app.register_blueprint(posts_blueprint)
	app.register_blueprint(signup_blueprint)
blueprints()
