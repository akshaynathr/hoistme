 
import sys
from login.views import signUp
from flask import Flask
from post.views import posts

#sys.path.append(__file__)

app=Flask(__name__)
app.register_blueprint(signUp)
app.register_blueprint(posts)

if __name__=="__main__":
	app.run(debug=True)
