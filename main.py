import json


class Student:

    def __int__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


class Course:
    def __init__(self, name):
        self.name = name


class Teacher:
    def __init__(self, name, course, salary):
        self.name = name
        self.course = course
        self.salary = salary


class Register:
    def __init__(self, student_name, course_name):
        self.student_name = student_name
        self.course_name = course_name


choice1 = input("if you want to add an object enter (add), if you want to register a student in a course enter (reg) ")

if choice1 == "add":
    print("what do you want to add ? ")
    choice2 = input("s for student, c for a course, t for a teacher ")

    if choice2 == 's':
        student1 = Student
        student1.name = input("enter student name: ")
        student1.age = input("enter student age: ")
        student1.grade = input("enter student grade: ")

        full_object = [student1.name, student1.age, student1.grade]

        with open('student.Json', 'a') as outfile:
            outfile.write(json.dumps(full_object))
            outfile.write(",")
            outfile.close()

    elif choice2 == 'c':
        course1 = Course
        course1.name = input("enter course name : ")
        with open('course.Json', 'a') as outfile:
            outfile.write(json.dumps(course1.name))
            outfile.write(",")
            outfile.close()

    elif choice2 == 't':

        obj_name = Teacher
        obj_name.name = input("  please enter teacher name: ")
        obj_name.course = input("  please enter what course this teacher teaches: ")
        obj_name.salary = input("  enter teacher salary: ")

        full_object = [obj_name.name, obj_name.course, obj_name.salary]

        with open('teacher.json', 'a') as outfile:
            outfile.write(json.dumps(full_object))
            outfile.write(",")
            outfile.close()

    else:
        print("please enter a valid letter ")

elif choice1 == "reg":
    reg1 = Register
    reg1.student_name = input("enter the student name")
    reg1.course_name = input("enter the course name")

    full_object = [reg1.student_name, reg1.course_name]

    with open('regester.json', 'a') as outfile:
        outfile.write(json.dumps(full_object))
        outfile.write(",")
        outfile.close()

else:
    print("please enter a valid choice ")
