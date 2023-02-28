from flask import Flask, request
from blog.report.views import report
from blog.user.views import user
import config

#app = Flask(__name__)


#@app.route('/', methods=['GET'])
#def index():
#    if request.method == 'GET':
#        config.count += 1
        
#    return f'Посещение {config.count}'


def create_app() -> Flask:
    app = Flask(__name__)
    app.run(
        host='127.0.0.1',
        debug=True,
    )
    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    app:register_blueprint(user)
    app:register_blueprint(report)
