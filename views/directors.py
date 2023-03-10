from flask import request
from flask_restx import Namespace, Resource

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace("directors")

@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        result = DirectorSchema(many=True).dump(directors)
        return result, 200


@director_ns.route("/<int:did>")
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_by_id(did)
        result = DirectorSchema(many=True).dump(director)
        return result, 200
