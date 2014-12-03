from server import app
 
from server import db
from flask import request
class Person(db.Document):
	name=db.StringField()


@app.route('/test1',methods=['GET'])
def test1():
	collection=Person._get_collection()
	#print(collection.find_one())
	return  'recieved'

@app.route('/test',methods=['PUT'])
def test():
	p=Person()
	p.name=request.form['name']
	return 'name_saved'	
	
