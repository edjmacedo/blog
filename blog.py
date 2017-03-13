import webapp2
from google.appengine.ext import db
from app.blog_handler import BlogHandler
from app.post_database import Post
from app.user_database import User
from app.login import Login
from app.signup import Signup
from app.logout import Logout
from app.new_post import NewPost
from app.post_page import PostPage

### Blog Home Page
class BlogFront(BlogHandler):
    def get(self):
        if self.user:
            posts = db.GqlQuery("select * from Post order by created desc limit 10")
            self.render('front.html', posts=posts)
        else:
            self.redirect("/login")

app = webapp2.WSGIApplication([('/?', BlogFront),
                               ('/([0-9]+)', PostPage),
                               ('/newpost', NewPost),
                               ('/signup', Signup),
                               ('/login', Login),
                               ('/logout', Logout)
                               ],
                              debug=True)
