
class MovieService:
    def __init__(self, movie_dao):
        self.movie_dao = movie_dao

    def get_all_movies(self, filters):

        return self.movie_dao.get_all(filters)

    def update(self, data):
        id = data.pop("id")
        movie = self.movie_dao.get_one(id)

        for field_name, field_value in data.items():
            setattr(movie, field_name, field_value)

        return self.movie_dao.update(movie)

    def create(self, data):
        return self.movie_dao.create(data)

    def get_by_id(self, id):
        return self.movie_dao.get_one(id)

    def delete(self, id):
        movie = self.movie_dao.get_one(id)
        return self.movie_dao.delete(movie)
