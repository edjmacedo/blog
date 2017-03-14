from blog_handler import BlogHandler

## Class to handle logout action
class Logout(BlogHandler):
    def get(self):
        self.logout()
        self.redirect('/login')