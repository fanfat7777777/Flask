from flask import Blueprint, render_template, redirect, session, escape
from flask_login import login_required
from werkzeug.exceptions import NotFound
import config


user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

#USERS = {
#    1: 'Alice',
#    2: 'Jon',
#    3: 'Mike',
#}

@user.route('/')
def user_list():
    if user in session:
        return 'Logged in as %s' % escape(session[user])
    return 'You are not logged in'

    from blog.models import User
    users = User.query.all()
    config.count += 1
    return render_template(
        'users/list.html',
        users=users,
        count=config.count,
        )

@user.route('/<int:pk>')
@login_required
def profile(pk: int):
    from blog.models import User
    
    _user = User.query.filter_by(id=pk).one_or_none()

    if user in session:
        return 'Logged in as %s' % escape(session[user])
    return 'You are not logged in'
    
    return render_template(
        'users/profile.html',
        user=_user,
        )