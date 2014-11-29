from login import views
from flask.ext.mongoengine import MongoEngine
import login
from main import app



app.config["MONGODB_SETTINGS"]={'db':'hoistme'}
app.config["SECRET_KEY"]="akshaynathr"

db=MongoEngine(app)

