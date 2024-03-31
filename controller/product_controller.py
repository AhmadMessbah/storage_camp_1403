from controller.validator import name_validator
from model.da.product_data import ProductData


def save_product(name, brand, quantity, buyer_price, seller_price):
    try:
        if name_validator(name) and name_validator(brand):
            data = ProductData()
            data.save(name, brand, quantity, buyer_price, seller_price)
            return True, "Saved"
        else:
            return False, "Error : Invalid Data"
    except Exception as e:
        return False, f"Error : {e}"


def edit_product(id, name, brand, quantity, buyer_price, seller_price):
    try:
        if name_validator(name) and name_validator(brand):
            data = ProductData()
            data.edit(id, name, brand, quantity, buyer_price, seller_price)
            return True, "Edited"
        else:
            return False, "Error : Invalid Data"
    except Exception as e:
        return False, f"Error : {e}"


def remove_product(id):
    try:
        data = ProductData()
        data.remove(id)
        return True, "Removed"
    except Exception as e:
        return False, f"Error : {e}"


def find_all():
    try:
        data = ProductData()
        return True, data.find_all()
    except Exception as e:
        return False, f"Error : {e}"


def find_by_id(id):
    try:
        data = ProductData()
        return True, data.find_by_id(id)
    except Exception as e:
        return False, f"Error : {e}"
