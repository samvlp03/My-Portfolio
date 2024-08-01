from os import environ
from My_Portfolio import app
from My_Portfolio.views import db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

