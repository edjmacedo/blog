from user_database import User
from blog_handler import BlogHandler
from utils import *
from comment_database import Comment

## Handle post page
## - render post page in permalink template
## - post comment in a post blog
class PostPage(BlogHandler):
    def get(self, post_id):
        if self.user:
            key = db.Key.from_path('Post', int(post_id), 
                                   parent=blog_key())
            post = db.get(key)

            if not post:
                self.error(404)
                return
            comments = db.GqlQuery("select * from Comment where post_id = "
                                   + post_id)
            self.render("permalink.html", post = post, comments = comments)
        else:
            self.redirect("/")
            
    def post(self, post_id):
        if self.user:
            content = self.request.get("content")
            if content:
                usr_comment = Comment(content = str(content),
                                      author = int(
                                          self.read_secure_cookie('user_id')
                                      ), post_id = int(post_id))
                usr_comment.put()
                self.redirect("/%s" % post_id)
            else:
                self.redirect("/")
        else:
            self.redirect("/")