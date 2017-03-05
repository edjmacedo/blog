import os
import re
import random
import sys
from string import letters

import webapp2
import jinja2
import hashlib
import hmac
from google.appengine.ext import db
sys.path.insert(0, './app')
import utils
from post_database import Post

SECRET = "imsosecret"


class BlogHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        u = utils.Utils()
        return u.render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
    
    def set_secure_cookie(self, name, val):
        cookie_val = make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val)
        )
    
    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val)
    
    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))
        
    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')
        
    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        self.user = uid and User.by_id(int(uid))

#def render_post(response, post):
#    response.out.write('<b>' + post.subject + '</b><br>')
#    response.out.write(post.content)

##### blog stuff

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)
   

class BlogFront(BlogHandler):
    def get(self):
        posts = db.GqlQuery("select * from Post order by created desc limit 10")
        self.render('front.html', posts = posts)

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
            
#class Signup(BlogHandler):
#    def get(self):
#        self.render("signup-form.html")

#    def post(self):
#        have_error = False
#        self.username = self.request.get('username')
#        self.password = self.request.get('password')
#        self.verify = self.request.get('verify')
#        self.email = self.request.get('email')

#        params = dict(username = self.username,
#                      email = self.email)

#        if not valid_username(self.username):
#            params['error_username'] = "That's not a valid username."
#            have_error = True

#        if not valid_password(self.password):
#            params['error_password'] = "That wasn't a valid password."
#            have_error = True
#        elif self.password != self.verify:
#            params['error_verify'] = "Your passwords didn't match."
#            have_error = True

#        if not valid_email(self.email):
#            params['error_email'] = "That's not a valid email."
#            have_error = True

#        if have_error:
#            self.render('signup-form.html', **params)
#        else:
#            self.done()

#   def done(self, *a, **kw):
#        raise NotImplementedError

#class Unit2Signup(Signup):
#    def done(self):
#        self.redirect('/unit2/welcome?username=' + self.username)
        
#class Register(Signup):
#    def done(self):
        #make sure the user doesn't already exist
#        u = User.by_name(self.username)
#        if u:
#            msg = 'That user already exists.'
#            self.render('signup-form.html', error_username = msg)
#        else:
#            u = User.register(self.username, self.password, self.email)
#            u.put()

#            self.login(u)
#            self.redirect('/blog/welcome')

#class Unit3Welcome(BlogHandler):
#    def get(self):
#        if self.user:
#            self.render('welcome.html', username = self.user.name)
#       else:
#            self.redirect('/blog/signup')

class Login(BlogHandler):
    def get(self):
        self.render('login-form.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/')
        else:
            msg = 'Invalid login'
            self.render('login-form.html', error = msg)
            
#class Logout(BlogHandler):
#    def get(self):
#        self.logout()
#        self.redirect('/blog/signup')


app = webapp2.WSGIApplication([('/?', BlogFront),                                                              
                               #('/blog/([0-9]+)', PostPage),
                               #('/blog/newpost', NewPost),
                               #('/blog/signup', Register),
                               #('/blog/welcome', Unit3Welcome),
                               ('/login', Login),
                               #('/blog/logout', Logout)
                               ],
                              debug=True)
