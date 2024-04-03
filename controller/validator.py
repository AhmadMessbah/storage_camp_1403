import re


def name_validator(name):
    return bool(re.match(r'^[a-zA-Z]{3,30}$', name))


def phone_validator(number):
    return bool(re.match(r'^(09|\+989)\d{9}$', number))
