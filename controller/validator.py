import re


def name_validator(name):
    return bool(re.match(r'^[a-zA-Z\s]{3,30}$', name))


def phone_number_validator(number):
    return bool(re.match(r'^(09|\+989)\d{9}$', number))
