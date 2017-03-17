from google.appengine.ext import db
from db_user import User
from utils import *

# Comment database
class Comment(db.Model):
    post_id = db.IntegerProperty(required = True)
    author = db.IntegerProperty(required = True)
    username = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    
    def render(self, userid):
        self._render_text = self.content.replace('\n','<br>')
        return render_str("comments.html", c = self, userid = userid)