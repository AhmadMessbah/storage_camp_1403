from tkinter import Tk, Button
import tkinter.messagebox as msg
from components import *
import controller.person_controller as p_control

from new_window import *
def person_click():
    open_person("Person")
def stuff_click():
    open_stuff("Stuff")
def transaction_click():
    open_transaction("Transaction")


win = Tk()
win.title("Library")
win.geometry("500x400")


Button(win,
       text="person",
       width=15,
       height=2,
       bg="lightgreen",
       font=("Arial", 16),
       command=person_click).place(x=170, y=100)

Button(win,
       text="stuff",
       width=15,
       height=2,
       bg="lightgreen",
       font=("Arial", 16),
       command=stuff_click).place(x=170, y=200)

Button(win,
       text="transaction",
       width=15,
       height=2,
       bg="lightgreen",
       font=("Arial", 16),
       command=transaction_click).place(x=170, y=300)
win.mainloop()