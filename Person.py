class Person:

    def __init__(self, id: int, name: str, last_name: str, birth_date: str, gender: int, status: int):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.staus = status

    def parse_to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastName": self.last_name,
            "birthDate": self.birth_date,
            "gender": self.gender,
            "status": self.staus
        }
