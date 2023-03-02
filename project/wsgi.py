from blog.app import create_app, db
from werkzeug.security import generate_password_hash
from blog.models import User

#if __name__ == '__main__':
#    app.run(
#        host='0.0.0.0',
#        debug=True,
#    )

app = create_app()

@app.cli.command('init-db')
def init_db():
    db.create_all()

@app.cli.command('create-users')
def create_users():
    db.session.add(
        User(
            email='name@mail.ru',
            password=generate_password_hash('123'),
            username='Test_User'
        )
    )
    db.session.commit()