from faker import Faker
import json

fake = Faker(['en-US'])

class User(object):
    def __init__(self, email, password, token = None) -> None:
        self.email = email
        self.password = password
        self.token = token

    def __str__(self) -> str:
        return json.dumps(self.__dict__)
    
def fake_user():
    email = f"{str(fake.email()).lower()}"
    password = f"{email}{fake.port_number()}"
    return User(email = email, password = password)