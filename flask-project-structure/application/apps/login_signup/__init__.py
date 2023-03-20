from flask_login import LoginManager


def UserProfile(app):
    login_manager = LoginManager()
    login_manager.login_view = 'loginSignup.login'
    login_manager.init_app(app)
    
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))