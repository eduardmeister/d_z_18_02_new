
class DirectorService:
    def __init__(self, director_dao):
        self.director_dao = director_dao

    def get_all(self):
        return self.director_dao.get_all()

    def get_by_id(self, id):
        return self.director_dao.get_one(id)
