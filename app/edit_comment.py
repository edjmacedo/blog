from db_user import User
from blog_handler import BlogHandler
from utils import *
from db_comment import Comment
import time

## Class to edit comment
class EditComment(BlogHandler):
    def get(self, post_id, comment_id):
        if self.user:
            ## Getting current comment using key
            key = db.Key.from_path('Comment', int(comment_id),
                                   parent=blog_key())
            c = db.get(key)
            ## Render comment in a textarea
            self.render("editcomment.html", content = c.content)
        else:
            self.redirect("/")
            
    def post(self, post_id, comment_id):
        ## Getting the current comment
        key = db.Key.from_path('Comment', int(comment_id),
                               parent=blog_key())
        c = db.get(key)
        ## Getting the text value inserted in textarea
        content = self.request.get("content")
        if content:
            ## Replace and update the comment
            c.content = content            
            c.put()
            time.sleep(0.1)
            self.redirect("/%s" % post_id)
        else:
            error = "Comment content is necessary"
            self.render("editcomment.html", content = content, error = error)