class Person:
    def __init__(self, my_id, name, age, nationality, lvl_of_education):
        self.my_id = my_id
        self.name = name
        self.age = age
        self.nationality = nationality
        self.lvl_of_education = lvl_of_education


class Student(Person):

    def __init__(self, my_id, name, age, nationality, lvl_of_education, gpa):
        super().__init__(my_id, name, age, nationality, lvl_of_education)
        self.GPA = gpa


class Course:
    def __init__(self, co_id, co_code, co_name, lecturer, room, duration, time):
        self.co_id = co_id
        self.co_code = co_code
        self.co_name = co_name
        self.lecturer = lecturer
        self.room = room
        self.duration = duration
        self.time = time


class Teacher(Person):

    def __init__(self, my_id, name, age, nationality, lvl_of_education, salary):
        super().__init__(my_id, name, age, nationality, lvl_of_education)
        self.salary = salary


class Register:
    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id
