import tkinter as tk

from view.person_window import TestForm
import tkinter.messagebox as msg

# Functions for opening new pages

def open_stuff_form():
    msg.showwarning("Message", "Under Construction")

def open_person(title):
    person = tk.Toplevel(win)
    person.title(title)
    person.title("Person")
    return person


def open_stuff(title):
    open_stuff = tk.Toplevel(win)
    open_stuff.title(title)
    open_stuff.title("Stuff")
    return open_stuff


def open_transaction(title):
    open_transaction = tk.Toplevel(win)
    open_transaction.title(title)
    open_transaction.title("Transaction")
    return open_transaction


def create_new_window(title):
    if title == "Person":
        open_person(title)
    elif title == "Stuff":
        open_stuff(title)
    elif title == "Transaction":
        open_transaction(title)


def open_person_form():
    TestForm()


win = tk.Tk()
win.geometry("300x300")
win.title("Main Window")

btn_person = tk.Button(win, text="Person", command=open_person_form, height=2, width=10)
btn_person.pack()

btn_stuff = tk.Button(win, text="Stuff", command=open_stuff_form, height=2, width=10)
btn_stuff.pack()

btn_transactions = tk.Button(win, text="Transactions", command="", height=2, width=10)
btn_transactions.pack()

win.mainloop()
