from db_user import User
from blog_handler import BlogHandler
from utils import *
from db_comment import Comment
from db_like import Like
import time


## Class to delete post
class DeletePost(BlogHandler):
    def get(self, post_id):
        if self.user:
            ## Getting post key using post_id and user_id
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            ## Searching and getting all likes relative to current post
            like = db.GqlQuery("select * from Like where post_id = "
                               + post_id)
            ## Getting all comments relative to current post
            comment = db.GqlQuery("select * from Comment where post_id = "
                                 + post_id)
            ## delete all comments, like and post
            db.delete(comment)
            db.delete(like)
            db.delete(post)
            time.sleep(0.1)
            self.redirect("/")
        else:
            self.redirect("/")