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
    children:list

    def __init__(self, name:string, surname:string, sex:string, birt_date:date, father:object, mother, age:int):
        self.father = father
        self.age = age
        self.mother = mother
        self.birth_date = birt_date
        self.surname = surname
        self.sex = sex
        self.name = name
        self.age = age
