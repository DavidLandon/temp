from faker import Faker
import json

fake = Faker(['en-US'])

class User(object):
    def __init__(self, id, password, token = None) -> None:
        self.id = id
        self.password = password
        self.token = token

    def __str__(self) -> str:
        return json.dumps(self.__dict__)
    
def fake_user():
    id = f"{str(fake.id())}"
    password = f"{id}{fake.port_number()}"
    return User(id = id, password = password)