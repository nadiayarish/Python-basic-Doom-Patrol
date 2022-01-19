# 1
from typing import Any


class Laptop:
    def __init__(self):
        battery_state1 = Battery("Charging")
        battery_state2 = Battery("Not charging")
        self.battery_states = (battery_state1, battery_state2)


class Battery:
    def __init__(self, status):
        self.status = status


keyboard = Laptop()
print(keyboard.battery_states[0].status)


# Charging

# 2
class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:

    def __init__(self):
        pass


guitar_string = GuitarString()
guitar = Guitar(guitar_string)


# 3
class Calc():
    @staticmethod
    def add_num(a, b, c):
        return a + b + c


print(Calc.add_num(5, 9, 20))


# 4*.

class Pasta:
    def __init__(self, list_of_ingredients):
        self.list_of_ingredients = list_of_ingredients

    def __str__(self):
        return f"This pasta contain {list_of_ingredients}"

    @classmethod
    def bolognaise(cls):
        return ["bacon", "parmesan", "eggs"]

    @classmethod
    def carbonara(cls):
        return ["forcemeat", "tomatoes"]


pasta_c = Pasta.carbonara()
print(pasta_c)


# 5
class Concert:
    max_visitors_num = 0

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value < self.max_visitors_num:
            self._visitors_count = value
        else:
            self._visitors_count = self.max_visitors_num


# 6.
import dataclasses


@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


person = AddressBookDataClass(key=3, name="Adam", phone_number="342-5334-232", address="Shevchenka St.",
                              email="adamdadam@gmail.com", birthday="2.12.1999", age=22)
print(person.name)  # Adam

# 7.
from collections import namedtuple

AddressBookDataClass = namedtuple("AddressBookDataClass", ["key", "name", "phone_number",
                                                           "address", "email", "birthday", "age"])

adam = AddressBookDataClass(2, "Adam", "342-5334-232", "Shevchenka St.", "adamdadam@gmail.com", "2.12.1999", 22)
print(adam.email)  # adamdadam@gmail.com


# 8.
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f"{self.key}, {self.name}, {self.phone_number}, {self.address}, {self.email}," \
               f"{self.birthday}, {self.age}"


company = AddressBook(45, "GlobalFunding", "344-455-234", "New York", "globalbobal@gmail.com", "01.01.2020", 2)
print(company.email)  # globalbobal@gmail.com


# 9.
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    @property
    def person_info(self):
        return f"{self.name} is {self.age} years old."


person1 = Person("John", 36, "USA")
person1.age = 40
print(person1.person_info)


# 10.
class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(143, "Natasha")
setattr(student, "email", "natashashasha@gmail.com")
print(getattr(student, "email"))


# 11
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def converter(self):
        return self._temperature * 1.8 + 32


temperature_today = Celsius(45)
print(temperature_today.converter)
