from blog_handler import BlogHandler
from user_database import User
from utils import *

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