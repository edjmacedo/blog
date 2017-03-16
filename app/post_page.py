from db_user import User
from blog_handler import BlogHandler
from utils import *
from db_comment import Comment
from db_like import Like
import time

## Handle post page
## - render post page in permalink template
## - post comment in a post blog
class PostPage(BlogHandler):
    def get(self, post_id):
        like = None
        if self.user:
            key = db.Key.from_path('Post', int(post_id), 
                                   parent=blog_key())
            post = db.get(key)

            if not post:
                self.error(404)
                return
            comments = db.GqlQuery("select * from Comment where post_id = "
                                   + post_id)
            like = db.GqlQuery("select * from Like where post_id = "
                              + post_id + " and author = " 
                              + self.read_secure_cookie('user_id')
                              ).get()            
            c_like = db.GqlQuery("select * from Like where post_id = "
                               + post_id)
            self.render("permalink.html", post = post, comments = comments, like = like,
                       userid = int(self.read_secure_cookie('user_id')), 
                       cLikes = c_like.count())
        else:
            self.redirect("/")
            
    def post(self, post_id):
        if self.user:
            if self.request.get("like"):
                usr_like = Like(post_id = int(post_id),
                               author = int(
                                self.read_secure_cookie('user_id')
                                )
                               )
                usr_like.put()
                time.sleep(0.1)
                self.redirect("/%s" % post_id)
            elif self.request.get("unlike"):
                like = db.GqlQuery("select * from Like where post_id = "
                                + post_id + " AND author = "
                                + self.read_secure_cookie('user_id'))
                db.delete(like)
                time.sleep(0.1)
                self.redirect("/%s" % post_id)
            else:
                content = self.request.get("content")
                if content:
                    usr_comment = Comment(parent = blog_key(), 
                                          content = str(content),
                                          author = int(
                                              self.read_secure_cookie('user_id')
                                          ), 
                                          username = self.user.name, 
                                          post_id = int(post_id)
                                         )
                    usr_comment.put()
                    time.sleep(0.1)
                    self.redirect("/%s" % post_id)
                else:
                    error = "You need input you comment"
                    key = db.Key.from_path('Post', int(post_id), 
                                   parent=blog_key())
                    post = db.get(key)            
                    comments = db.GqlQuery("select * from Comment where post_id = "
                                   + post_id)
                    like = db.GqlQuery("select * from Like where post_id = "
                              + post_id + " and author = " 
                              + self.read_secure_cookie('user_id')
                              ).get()            
                    c_like = db.GqlQuery("select * from Like where post_id = "
                               + post_id)
                    self.render("permalink.html", post = post, comments = comments, like = like,
                       userid = int(self.read_secure_cookie('user_id')), 
                       cLikes = c_like.count(), error = error)                   
        else:
            self.redirect("/")