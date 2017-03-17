from db_user import User
from blog_handler import BlogHandler
from utils import *
from db_comment import Comment
import time

## Class to delete comment of post
class DeleteComment(BlogHandler):
    def get(self, post_id, comment_id):
        if self.user:
            ## Getting comment key using comment_id
            key = db.Key.from_path('Comment', int(comment_id),
                                   parent=blog_key())
            c = db.get(key)            
            c.delete()
            self.redirect("/"+post_id)
        else:
            self.redirect("/")