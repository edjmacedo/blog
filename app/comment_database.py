from google.appengine.ext import db
from user_database import User
from utils import *

# Comment database
class Comment(db.Model):
    post_id = db.IntegerProperty(required = True)
    author = db.IntegerProperty(required = True)
    content = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    
    def render(self):
        self._render_text = self.content.replace('\n','<br>')
        return render_str("comments.html", c = self)