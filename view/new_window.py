import tkinter as tk

def open_person(title):
    person = tk.Toplevel()
    person.title(title)
    person.title("Person")
    return person

def open_stuff(title):
    open_stuff = tk.Toplevel()
    open_stuff.title(title)
    open_stuff.title("Stuff")
    return open_stuff

def open_transaction(title):
    open_transaction = tk.Toplevel()
    open_transaction.title(title)
    open_transaction.title("Transaction")
    return open_transaction

def create_new_window(title, win):
    if title == "Person":
        open_person(title)
    elif title == "Stuff":
        open_stuff(title)
    elif title == "Transaction":
        open_transaction(title)

def create_button(name, win):
    def on_button_click():
        create_new_window(name, win)
    return on_button_click
