from flask import Flask
from database import database
from apps.login_signup import  views, UserProfile
from apps.home import home


def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.DevelopmentConfig')
    database.init_app(app)
    
    UserProfile(app)
    
    app.register_blueprint(views.loginSignup)
    app.register_blueprint(home.home)
    # app.register_blueprint(app2, url_prefix="/app2")
    
    return app

if __name__ == '__main__':
    create_app().run()
    

