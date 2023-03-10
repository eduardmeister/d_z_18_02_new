from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, filters):
        if filters["director_id"]:
            return self.session.query(Movie).filter(Movie.director_id == filters["director_id"]).all()
        elif filters["genre_id"]:
            return self.session.query(Movie).filter(Movie.genre_id == filters["genre_id"]).all()
        elif filters["year"]:
            return self.session.query(Movie).filter(Movie.year == filters["year"]).all()

        return self.session.query(Movie).all()

    def get_one(self, id):
        return self.session.query(Movie).get(id)

    def update(self, movie):

        self.session.add(movie)
        self.session.commit()
        return movie

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()




