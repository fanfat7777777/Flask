from flask import Blueprint, render_template, redirect

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: 'Статья 1',
    2: 'Статья 2',
    3: 'Статья 3',
    4: 'Статья 4',
    5: 'Статья 5',
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
    )