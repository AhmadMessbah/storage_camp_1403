import tkinter as tk

# Functions for opening new pages
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

def create_button(name):
    def on_button_click():
        create_new_window(name)
    return on_button_click

win = tk.Tk()
win.geometry("300x300")
win.title("Main Window")

buttons = ["Person", "Stuff", "Transaction"]
for button in buttons:
    tk.Button(win, text=button, command=create_button(button), height=2, width=10).pack()

win.mainloop()
