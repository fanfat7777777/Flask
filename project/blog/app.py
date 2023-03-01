from flask import Flask, request
from blog.report.views import report
from blog.user.views import user
from blog.articles.views import article
import config

#app = Flask(__name__)


#@app.route('/', methods=['GET'])
#def index():
#    if request.method == 'GET':
#        config.count += 1
        
#    return f'Посещение {config.count}'


def create_app() -> Flask:
    app = Flask(__name__)
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
