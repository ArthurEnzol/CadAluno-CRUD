from datetime import date

class Student:
    def __init__(self, id_: None, username: str, age: int, school: str, grade: int):
        self.id = id_
        self.username = username
        self.age = age
        self.school = school
        self.grade = grade

class Responsable:
    def __init__(self, id_: None,name: str, number: int, pay: str, pay_day: date, children: str):
        self.id = id_
        self.name = name
        self.number = number
        self.pay = pay
        self.pay_day = pay_day
        self.children = children

