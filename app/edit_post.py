from db_user import User
from blog_handler import BlogHandler
from db_post import Post
from utils import *
import time

class EditPost(BlogHandler):
    def get(self, post_id):
        if self.user:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            self.render("newpost.html", subject = post.subject, content = post.content,
                       action = "Edit Post")
        else:
            self.redirect("login")

    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
            
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            post.subject = subject
            post.content = content
            post.put()
            time.sleep(0.1)
            self.redirect('/%s' % str(post.key().id()))
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject, content=content,
                        error=error)