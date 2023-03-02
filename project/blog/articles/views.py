from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
#from blog.user.views import USERS

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: {
        'name': 'Статья 1',
        'text': 'text',
        'author': 1,
        },
    2: {
        'name': 'Статья 2',
        'text': 'text',
        'author': 2,
        },
    3: {
        'name': 'Статья 3',
        'text': 'text',
        'author': 3,
        },
    4: {
        'name': 'Статья 4',
        'text': 'text',
        'author': 1,
        },
}

@article.route('/')
def article_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES,
    )

@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        article_name=ARTICLES[pk]
    except:
        raise NotFound(f'Article id {pk} not found')
    
    return render_template(
        'articles/details.html',
        article_name=article_name,
        #article_author=USERS[article_name['author']],
    )