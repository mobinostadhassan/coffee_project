import re
from datetime import datetime


def name_validator(name):
    if type(name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", name):
        return name
    else:
        raise ValueError("Invalid Name !!!")


def code_validator(code):
    if type(code) == int:
        return code
    else:
        raise ValueError("Invalid code !!!")


def day_validator(day):
    if day in ["shanbeh", "1shanbeh", "2shanbeh", "3shanbeh", "4shanbeh", "5shanbeh", "jomeh"]:
        return day
    else:
        raise ValueError("Invalid day !!!")


def time_validator(time):
    try:
        if type(time) == datetime:
            return datetime.strptime(time, "%H:%M ")
    except:
        raise ValueError("Invalid Time !!!")


def teacher_validator(teacher):
    if type(teacher) == str and re.match(r"^[a-zA-Z\s]{3,30}$", teacher):
        return teacher
    else:
        raise ValueError("invalid teacher !!!")


def duration_validator(duration):
    try:
        if type(duration) == int:
            return duration
    except:
        raise ValueError("Invalid duration !!!")