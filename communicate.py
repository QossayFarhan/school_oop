
import json


def open_student():
    with open("jsons/student.Json", "r") as read_file:
        s_data = json.load(read_file)
    return s_data


def add_st_json(full_object):
    open_student()
    s_data = open_student()

    s_data.append(full_object)

    with open("jsons/student.Json", "w+") as jsonFile:
        jsonFile.write(json.dumps(s_data))


def open_teacher():
    with open("jsons/teacher.json", "r") as teacher_file:
        t_data = json.load(teacher_file)
    return t_data


def add_te_json(full_object):
    data = open_teacher()
    data.append(full_object)

    with open("jsons/teacher.json", "w+") as jsonFile:
        jsonFile.write(json.dumps(data))


def open_course():
    with open("jsons/course.Json", "r") as read_course:
        c_data = json.load(read_course)
    return c_data


def add_co_json(full_object):

    data = open_course()

    data.append(full_object)

    with open("jsons/course.Json", "w+") as jsonFile:
        jsonFile.write(json.dumps(data))


def reg_json(student_id, course_id):
    with open("jsons/regester.json", "r") as read_file:
        data = json.load(read_file)

        pair = [student_id, course_id]
        data.append(pair)

    with open("jsons/regester.json", "w+") as jsonFile:
        jsonFile.write(json.dumps(data))

