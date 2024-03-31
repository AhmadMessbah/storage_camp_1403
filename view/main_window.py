from tkinter import *
from view.person_window import PersonForm
from view.product_window import ProductForm


def open_person(title):
    person = Toplevel(win)
    person.title(title)
    person.title("Person")
    return person


def open_product(title):
    product = Toplevel(win)
    product.title(title)
    product.title("Stuff")
    return product


def open_transaction(title):
    transactions = Toplevel(win)
    transactions.title(title)
    transactions.title("Transaction")
    return open_transaction


def create_new_window(title):
    if title == "Person":
        open_person(title)
    elif title == "Stuff":
        open_product(title)
    elif title == "Transaction":
        open_transaction(title)


def open_person_form():
    PersonForm()


def open_product_form():
    ProductForm()


def open_transaction_form():
    TransactionForm()


win = Tk()
win.geometry("300x300")
win.title("Main Window")

btn_person = Button(win, text="Person", command=open_person_form, height=2, width=10)
btn_person.pack()

btn_product = Button(win, text="Product", command=open_product_form, height=2, width=10)
btn_product.pack()

btn_transactions = Button(win, text="Transactions", command=open_transaction_form, height=2, width=10)
btn_transactions.pack()

win.mainloop()
