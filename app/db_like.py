from google.appengine.ext import db
from db_user import User
from utils import *

# Like database
class Like(db.Model):
    post_id = db.IntegerProperty(required = True)
    author = db.IntegerProperty(required = True)