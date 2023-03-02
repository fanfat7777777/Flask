from flask import Flask, request, redirect, url_for, session, escape
from flask_sqlalchemy import SQLAlchemy
from blog.report.views import report
from blog.user.views import user
from blog.articles.views import article
from blog.auth.views import auth
from flask_login import LoginManager
import config

#app = Flask(__name__)


#@app.route('/', methods=['GET'])
#def index():
#    if request.method == 'GET':
#        config.count += 1
        
#    return f'Посещение {config.count}'




def create_app() -> Flask:
    app = Flask(__name__)
    db = SQLAlchemy()
    app.config['SECRET_KEY'] = '@ag=ii4#ek+^yb4_m8+z=fzjq^)bg#s@yso3vs6u*z603=t_70'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from blog.models import User

    @login_manager.user_loader
    def load_user(user_id):
        User.query.get(int(user_id))

#    @login_manager.unauthorized_handler
#    def unauthorized():
#        return redirect(url_for("auth.login"))

    register_blueprint(app)
    app.run(
        host='127.0.0.1',
        debug=True,
    )
    return app


def register_blueprint(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(article)
    app.register_blueprint(auth)
