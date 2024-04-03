from tkinter import *
from person_window import PersonForm
from product_window import ProductForm
from transaction_window import TransactionForm


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
