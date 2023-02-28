from flask import Flask, request
import config

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        config.count += 1
        
    return f'Посещение {config.count}'
