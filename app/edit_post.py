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
            if not post:
                return self.redirect('/')
            if post.author == int(self.read_secure_cookie('user_id')):                
                ## Render current post in a editting screen
                self.render("editpost.html", subject = post.subject, content = post.content,
                       action = "Edit Post", post_id = post_id)
            else:
                self.redirect("/")
        else:
            self.redirect("/")

    def post(self, post_id):
        if self.user:
            post = get_post_by_id(post_id)
            if not post:
                return self.redirect('/')
            ## Getting value inserted in textarea
            subject = self.request.get('subject')
            content = self.request.get('content')
            if post.author == int(self.read_secure_cookie('user_id')):
                if subject and content:
                    ## Replace and update current value with new value
                    post.subject = subject
                    post.content = content
                    post.put()
                    time.sleep(0.1)
                    self.redirect('/%s' % str(post.key().id()))
                else:
                    error = "subject and content, please!"
                    self.render("editpost.html", subject=subject, content=content,
                        error=error)
            else:
                self.redirect("/")
        else:
            self.redirect("/")