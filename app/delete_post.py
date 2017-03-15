from db_user import User
from blog_handler import BlogHandler
from utils import *
from db_comment import Comment
from db_like import Like
import time

class DeletePost(BlogHandler):
    def get(self, post_id):
        if self.user:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            like = db.GqlQuery("select * from Like where post_id = "
                               + post_id)
            comment = db.GqlQuery("select * from Comment where post_id = "
                                 + post_id)
            db.delete(comment)
            db.delete(like)
            db.delete(post)
            time.sleep(0.1)
            self.redirect("/")
        else:
            self.redirect("/")