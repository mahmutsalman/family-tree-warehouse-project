import string
from datetime import date


class Person:
    name: string
    surname: string
    age: int
    sex: string
    birth_date: date
    death_date: date
    father: object
    mother: object
    children: list

    def __init__(self, name: string):
        self.name = name
