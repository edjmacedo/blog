from db_user import User
from blog_handler import BlogHandler
from db_post import Post
from utils import *
import time


## Class to edit blog post
class EditPost(BlogHandler):
    def get(self, post_id):
        if self.user:
            ## Getting post using index key
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            ## Render current post in a editting screen
            self.render("newpost.html", subject = post.subject, content = post.content,
                       action = "Edit Post")
        else:
            self.redirect("login")

    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        
        ## Getting value inserted in textarea
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            ## Replace and update current value with new value
            post.subject = subject
            post.content = content
            post.put()
            time.sleep(0.1)
            self.redirect('/%s' % str(post.key().id()))
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject, content=content,
                        error=error)