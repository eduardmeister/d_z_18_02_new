from flask import Flask
from flask_restx import Api


from config import Config
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from views.movies import movies_ns
from views.genres import genres_ns
from views.directors import director_ns
from setup_db import db


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()
        d_1 = Director(id=1, name="Ivan Ivanoff")
        d_2 = Director(id=2, name="Petr Petroff")

        g_1 = Genre(id=1, name="Dich")
        g_2 = Genre(id=2, name="Dich_2")

        m_1 = Movie(id=1, title="Йеллоустоун", description = "Владелец",
                    trailer="https: // www.youtube.com / watch?v = UKei_d0cbP4",
                    year=2001, rating=8.6, director_id=1, genre_id=1)
        m_2 = Movie(id=2, title="Йеллоустоун_2", description="Владелец_2",
                    trailer="https: // www.youtube.com / watch?v = UKei_d0cbP4",
                    year=200, rating=8.6, director_id=2, genre_id=2)

        with db.session.begin():
            db.session.add_all([m_2, m_1])
            db.session.add_all([d_1, d_2])
            db.session.add_all([g_2, g_1])


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
