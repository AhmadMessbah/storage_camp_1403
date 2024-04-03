from controller.validator import *
from model.da.person_data import PersonData


def save_person(name, family, phone):
    try:
        if name_validator(name) and name_validator(family) and phone_validator(phone):
            data = PersonData()
            data.save(name, family, phone)
            return True, "Saved"
        else:
            return False, "Error : Invalid Data"
    except Exception as e:
        return False, f"Error : {e}"


def edit_person(person_id, name, family, phone):
    try:
        if name_validator(name) and name_validator(family) and phone_validator(phone):
            data = PersonData()
            data.edit(person_id, name, family, phone)
            return True, "Edited"
        else:
            return False, "Error : Invalid Data"
    except Exception as e:
        return False, f"Error : {e}"


def remove_person(id_to_remove):
    try:
        data = PersonData()
        data.remove(id_to_remove)
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
