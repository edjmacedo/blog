import webapp2
from google.appengine.ext import db
from app.blog_handler import BlogHandler
from app.db_post import Post
from app.db_user import User
from app.login import Login
from app.signup import Signup
from app.logout import Logout
from app.new_post import NewPost
from app.post_page import PostPage
from app.delete_post import DeletePost
from app.delete_comment import DeleteComment
from app.edit_post import EditPost
from app.edit_comment import EditComment

### Blog Home Page
class BlogFront(BlogHandler):
    def get(self):
        if self.user:
            posts = db.GqlQuery("select * from Post order by created desc limit 10")
            self.render('front.html', posts=posts, 
                        userid = int(self.read_secure_cookie('user_id')))
        else:
            self.redirect("/login")

app = webapp2.WSGIApplication([('/?', BlogFront),
                               ('/([0-9]+)', PostPage),
                               ('/newpost', NewPost),
                               ('/signup', Signup),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/delete/([0-9]+)', DeletePost),
                               ('/delete/([0-9]+)/([0-9]+)', DeleteComment),
                               ('/edit/([0-9]+)', EditPost),
                               ('/edit/([0-9]+)/([0-9]+)', EditComment)
                               ],
                              debug=True)
