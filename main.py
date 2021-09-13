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

        with open("student.Json", "r") as read_file:
            data = json.load(read_file)

            data['students'].append(full_object)

        with open("student.Json", "w+") as jsonFile:
            jsonFile.write(json.dumps(data))

    elif choice2 == 'c':
        course1 = Course
        course1.name = input("enter course name : ")
        with open("course.Json", "r") as read_file:
            data = json.load(read_file)

            data['cou'].append(course1.name)

        with open("course.Json", "w+") as jsonFile:
            jsonFile.write(json.dumps(data))

    elif choice2 == 't':

        obj_name = Teacher
        obj_name.name = input("  please enter teacher name: ")
        obj_name.course = input("  please enter what course this teacher teaches: ")
        obj_name.salary = input("  enter teacher salary: ")

        full_object = [obj_name.name, obj_name.course, obj_name.salary]

        with open("teacher.json", "r") as read_file:
            data = json.load(read_file)

            data['teachers'].append(full_object)

        with open("teacher.json", "w+") as jsonFile:
            jsonFile.write(json.dumps(data))

    else:
        print("please enter a valid letter ")

elif choice1 == "reg":
    reg1 = Register
    reg1.student_name = input("enter the student name")
    reg1.course_name = input("enter the course name")

    with open("student.Json", "r") as read_student:
        S_data = json.load(read_student)
        if reg1.student_name in [j for i in S_data['students'] for j in i]:
            student_check = True
        else:
            student_check = False
            print("student is not registered in the system ")

    with open("course.Json", "r") as read_course:
        C_data = json.load(read_course)
        if reg1.course_name in C_data['cou']:
            course_check = True
        else:
            print("course is not registered in the system")
            course_check = False

    if student_check is True & course_check is True:
        with open("regester.json", "r") as read_file:
            data = json.load(read_file)

            if reg1.course_name in data['reg']:
                data['reg'][reg1.course_name].append(reg1.student_name)
            else:
                data['reg'][reg1.course_name] = [reg1.student_name]

        with open("regester.json", "w+") as jsonFile:
            jsonFile.write(json.dumps(data))

else:
    print("please enter a valid choice ")
