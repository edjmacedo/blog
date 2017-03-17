from db_user import User
from blog_handler import BlogHandler
from db_post import Post
from utils import *


## Class to handle new post in blog home page
## - Check if user is logged and rander new post template
## - Get content and update Post Database
class NewPost(BlogHandler):
    def get(self):
        if self.user:
            self.render("newpost.html", action = "New Post")
        else:
            self.redirect("/")

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            p = Post(parent = blog_key(), subject = subject, 
                     content = content,
                     author = int(self.read_secure_cookie('user_id')))
            p.put()
            self.redirect('/%s' % str(p.key().id()))
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject, content=content,
                        error=error)