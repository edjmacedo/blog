from google.appengine.ext import db
from utils import *

# This class create post table in database
class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)
    author = db.IntegerProperty(required = True)
    
    def render(self, userid):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p = self,
                         userid = userid
                         )