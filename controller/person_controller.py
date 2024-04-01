from controller.validator import *
from model.da.person_data import PersonData


def save_person(name, family, phone):
    try:
        if name_validator(name) and name_validator(family) and phone_number_validator(phone):
            data = PersonData()
            data.save(name, family, phone)
            return True, "Saved"
        else:
            return False, "Error : Invalid Data"
    except Exception as e:
        return False, f"Error : {e}"


def edit_person(id, name, family, phone_number):
    try:
        if name_validator(name) and name_validator(family) and phone_number_validator(phone):
            data = PersonData()
            data.edit(id, name, family, phone_number)
            return True, "Edited"
        else:
            return False, "Error : Invalid Data"
    except Exception as e:
        return False, f"Error : {e}"


def remove_person(id):
    try:
        data = PersonDa()
        data.remove(id)
        return True, "Removed"
    except Exception as e:
        return False, f"Error : {e}"


def find_all():
    try:
        data = PersonData()
        return True, data.find_all()
    except Exception as e:
        return False, f"Error : {e}"


def find_by_id(id):
    try:
        data = PersonData()
        return True, data.find_by_id(id)
    except Exception as e:
        return False, f"Error : {e}"
