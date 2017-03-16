from db_user import User
from blog_handler import BlogHandler
from utils import *
from db_comment import Comment
import time

class EditComment(BlogHandler):
    def get(self, post_id, comment_id):
        if self.user:
            key = db.Key.from_path('Comment', int(comment_id),
                                   parent=blog_key())
            c = db.get(key)
            self.render("editcomment.html", content = c.content)
        else:
            self.redirect("/")
            
    def post(self, post_id, comment_id):
        key = db.Key.from_path('Comment', int(comment_id),
                               parent=blog_key())
        c = db.get(key)
        
        content = self.request.get("content")
        if content:
            c.content = content            
            c.put()
            time.sleep(0.1)
            self.redirect("/%s" % post_id)
        else:
            error = "Comment content is necessary"
            self.render("editcomment.html", content = content, error = error)