import re
from src.models.exceptions import ValidationError

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    @property
    def email(self):
        return self._email
    

    @email.setter
    def email(self, value):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if(not re.match(pattern, value)):
            raise ValidationError("Неверный формат email")
        self._email = value

    def set_email(self, value):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if(not re.match(pattern, value)):
            raise ValidationError("Неверный формат email")
        self._email = value

    def get_info(self):
        return f"Пользователь: {self.name}, Email: {self.email}"

