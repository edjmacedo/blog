from user_database import User
from blog_handler import BlogHandler
from post_database import Post
from utils import *

class NewPost(BlogHandler):
    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect("login")

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            p = Post(parent = blog_key(), subject = subject, content = content)
            p.put()
            self.redirect('/%s' % str(p.key().id()))
            #self.redirect('/')
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject, content=content, error=error)