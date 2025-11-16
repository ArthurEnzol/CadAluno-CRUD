import pymysql
import os
from model import Student, Responsable

connection = pymysql.connect(
    database= os.getenv("DATABASE"),
    user= os.getenv("DB_USER"),
    password= os.getenv("DB_PASSWORD"),
    host= os.getenv("DB_HOST"),
    port= os.getenv("DB_PORT"),
    charset=os.getevn("DB_CHARSET"),
    cursorclass= pymysql.cursors.DictCursor,
)

def save_student_dall(student: Student):
    with connection.cursor() as cursor:
        sql = """INSERT INTO student (username, age, school, grade) 
        VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql, (
            student.username,
            student.age,
            student.school,
            student.grade
        ))
        connection.commit()

def delete_student_dall(student: Student):
    with connection.cursor() as cursor:
        sql = """
        DELETE FROM student 
        WHERE id = (SELECT id WHERE username = %s)
        """
        cursor.execute(sql, (
            student.username
        ))
        connection.commit()

def update_student_dall(student: Student):
    with connection.cursor() as cursor:
        sql = """
            UPDATE student SET username = %s, age = %s, school = %s, grade = %s WHERE
            id = %s
        """
        cursor.execute(sql, (
            student.username,
            student.age,
            student.school,
            student.grade,
            student.id
        ))
        connection.commit()

def view_student_dall(name):
    with connection.cursor() as cursor:
        sql = """
            SELECT * FROM student WHERE username LIKE %s
        """
        cursor.execute(sql, (f"%{name}%",))
        result = cursor.fetchall()

    return result


def save_responsable_dall(responsable: Responsable):
    with connection.cursor() as cursor:
        sql = """
        INSERT INTO responsable (number, name, pay, pay_day, student_id)
        VALUES (%s, %s, %s, %s, 
        (SELECT id FROM student WHERE username = %s)
        )
        """
        cursor.execute(sql, (
            responsable.number,
            responsable.name,
            responsable.pay,
            responsable.pay_day,
            responsable.children
        ))
        connection.commit()

def delete_responsable_dall(responsable: Responsable):
    with connection.cursor() as cursor:
        sql = """
        DELETE FROM responsable
        WHERE id = (SELECT id WHERE name = %s)
        """
        cursor.execute(sql, (
            responsable.name
        ))
        connection.commit()

def update_responsable_dall(responsable: Responsable):
    with connection.cursor() as cursor:
        sql = """
        UPDATE responsable SET number = %s, name = %s, pay = %s, pay_day = %s 
        WHERE id = %s
        """
        cursor.execute(sql, (
            responsable.number,
            responsable.name,
            responsable.pay,
            responsable.pay_day,
            responsable.id
        ))
        connection.commit()

def view_responsable_dall(name):
    with connection.cursor() as cursor:
        sql = """
        SELECT * FROM responsable WHERE name = %s
        """
        cursor.execute(sql, name)
        result = cursor.fetchall()
    return result
