from flask import request
from flask_restx import Namespace, Resource

from dao.model.movie import MovieSchema
from implemented import movie_service
movies_ns = Namespace("movies")


@movies_ns.route("/")
class MoviesView(Resource):
    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filters = {
            "director_id" : director,
            "genre_id" : genre,
            "year" : year,
        }

        movies = movie_service.get_all_movies(filters)
        result = MovieSchema(many=True).dump(movies)

        return result, 200

    def post(self):
        req_data = request.json
        movie = movie_service.create(req_data)
        return "", 201


@movies_ns.route("/<int:mid>")
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_by_id(mid)
        result = MovieSchema().dump(movie)
        return result, 200

    def put(self, mid):
        req_data = request.json
        req_data["id"] = mid
        movie = movie_service.update(req_data)
        result = MovieSchema().dump(movie)
        return result, 204

    def delete(self, did):
        movie_service.delete(did)
        return "", 204