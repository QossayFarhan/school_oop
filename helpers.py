from prettytable import PrettyTable
from classes import *
from communicate import *


def choose():
    while True:
        print("select: "
              "1. ADD "
              "2. REGISTER ")
        choice = input("Answer:  ")
        if choice == "1":
            add()
        elif choice == "2":
            register()
        else:
            print("please enter a valid choice ")


def add():
    print("Select what to add ?"
          "1. STUDENT "
          "2. COURSE "
          "3. TEACHER  ")
    choice = input("Answer:  ")

    if choice == '1':
        add_student()
    elif choice == '2':
        add_course()
    elif choice == '3':
        add_teacher()
    else:
        print("please enter a valid choice ")


def add_student():
    student1 = Student
    s_data = open_student()
    st_id = ((s_data[len(s_data) - 1][0]) + 1)
    name = input("enter student name: ")
    age = int(input("enter student age: "))
    nationality = input("enter student nationality: ")
    level_of_education = input("enter student level of education: ")
    gpa = float(input("enter student gpa: "))
    student1(st_id, name, age, nationality, level_of_education, gpa)

    full_object = [st_id, name, age, nationality, level_of_education, gpa]

    add_st_json(full_object)

    print("student has been added successfully !")


def add_course():
    course1 = Course
    c_data = open_course()
    course1.course_id = ((c_data[len(c_data) - 1][0]) + 1)
    course1.co_code = input("enter course code: ")
    course1.co_name = input("enter course name: ")

    t_data = open_teacher()
    print("Teachers list:  ")
    teacher_table = PrettyTable(['Teacher ID', 'Teacher name'])
    for i in range(len(t_data)):
        teacher_table.add_row([t_data[i][0], t_data[i][1]])
    print(teacher_table)
    while True:
        course1.lecturer = int(input("enter the id of the lecturer of this course: "))
        if course1.lecturer in [j for i in t_data for j in i]:
            break
        else:
            print("the lecturer you have entered is not in the system, please reenter the teacher ID ")
    course1.room = input("enter the location of this course: ")
    course1.duration = input("enter the duration of this course: ")
    course1.time = input("enter the day and the time of this: ")

    full_object = [course1.course_id, course1.co_code, course1.co_name, course1.lecturer, course1.room, course1.duration, course1.time]

    add_co_json(full_object)
    print("course has been added successfully !")


def add_teacher():
    teacher1 = Teacher
    t_data = open_teacher()
    te_id = ((t_data[len(t_data) - 1][0]) + 1)
    name = input("enter teacher name: ")
    age = int(input("enter teacher age: "))
    nationality = input("enter teacher nationality: ")
    level_of_education = input("enter teacher level of education: ")
    salary = float(input("enter teacher salary: "))
    teacher1(te_id, name, age, nationality, level_of_education, salary)

    full_object = [te_id, name, age, nationality, level_of_education, salary]

    add_te_json(full_object)
    print("teacher has been added successfully !")


def register():
    reg1 = Register
    c_data = open_course()
    print("Courses list:  ")
    course_table = PrettyTable(['Course ID', 'Course code', 'Course name'])
    for i in range(len(c_data)):
        course_table.add_row([c_data[i][0], c_data[i][1], c_data[i][2]])
    print(course_table)
    reg1.student_id = int(input("enter the student id: "))
    reg1.course_id = int(input("enter the course id: "))

    s_data = open_student()
    if reg1.student_id in [j for i in s_data for j in i]:
        student_check = True
    else:
        student_check = False
        print("student is not registered in the system ")

    if reg1.course_id in [j for i in c_data for j in i]:
        course_check = True
    else:
        print("course is not registered in the system")
        course_check = False

    if student_check is True & course_check is True:
        reg_json(reg1.student_id, reg1.course_id)
        print("registration done successfully !")
