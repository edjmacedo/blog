import webapp2
from google.appengine.ext import db
from app.blog_handler import BlogHandler
from app.post_database import Post
from app.user_database import User
from app.login import Login
from app.signup import Signup
from app.logout import Logout

### Blog Home Page
class BlogFront(BlogHandler):
    def get(self):
        if self.user:
            posts = db.GqlQuery("select * from Post order by created desc limit 10")
            self.render('front.html', posts=posts)
        else:
            self.redirect("/login")

#class PostPage(BlogHandler):
#    def get(self, post_id):
#        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
#        post = db.get(key)

#        if not post:
#            self.error(404)
#            return

#        self.render("permalink.html", post = post)

#class NewPost(BlogHandler):
#    def get(self):
#        if self.user:
#            self.render("newpost.html")
#        else:
#            self.redirect("login")

#    def post(self):
#        subject = self.request.get('subject')
#        content = self.request.get('content')

#        if subject and content:
#            p = Post(parent = blog_key(), subject = subject, content = content)
#            p.put()
#            self.redirect('/blog/%s' % str(p.key().id()))
#        else:
#            error = "subject and content, please!"
#            self.render("newpost.html", subject=subject, content=content, error=error)


#   def done(self, *a, **kw):
#        raise NotImplementedError

#class Unit2Signup(Signup):
#    def done(self):
#        self.redirect('/unit2/welcome?username=' + self.username)
        
#class Register(Signup):
#    

#class Unit3Welcome(BlogHandler):
#    def get(self):
#        if self.user:
#            self.render('welcome.html', username = self.user.name)
#       else:
#            self.redirect('/blog/signup')


app = webapp2.WSGIApplication([('/?', BlogFront),                                                              
                               #('/blog/([0-9]+)', PostPage),
                               #('/blog/newpost', NewPost),
                               ('/signup', Signup),
                               #('/blog/welcome', Unit3Welcome),
                               ('/login', Login),
                               ('/logout', Logout)
                               ],
                              debug=True)
