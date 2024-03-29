from tkinter import Tk, Button
from tkinter import Tk, Button
import tkinter.messagebox as msg
from view.components import *


class TestForm:

    def __init__(self):
        win = Tk()
        win.geometry("300x400")

        def person_select(row):
            p_id.variable.set(row[0])
            p_name.variable.set(row[1])
            p_family.variable.set(row[2])

        def p_save_click():
            status, message = p_control.save(
                p_name.variable.get(),
                p_family.variable.get())

            if status:
                msg.showinfo("Save", message)
                refresh_person_side()
            else:
                msg.showerror("Save Error", message)

        def p_edit_click():
            status, message = p_control.edit(
                p_id.variable.get(),
                p_name.variable.get(),
                p_family.variable.get())

            if status:
                msg.showinfo("Edit", message)
                refresh_person_side()
            else:
                msg.showerror("Edit Error", message)

        def p_remove_click():
            status, message = p_control.remove(p_id.variable.get())

            if status:
                msg.showinfo("Remove", message)
                refresh_person_side()
            else:
                msg.showerror("Remove Error", message)

        # Person
        Label(win, text="Person Info", font=("Arial", 16)).place(x=20, y=10)
        p_id = TextAndLabel(win, "name", 20, 50)
        p_name = TextAndLabel(win, "family", 20, 85)
        p_family = TextAndLabel(win, "phone", 20, 120)

        p_table = Table(win,
                        None,
                        ["name", "family", "phone"],
                        [60, 100, 100],
                        20,
                        150,
                        person_select)
        Button(win, text="SavePerson", width=10, command=p_save_click).place(x=20, y=400)
        Button(win, text="EditPerson", width=10, command=p_edit_click).place(x=110, y=400)
        Button(win, text="RemovePerson", width=10, command=p_remove_click).place(x=200, y=400)

        # refresh_person_side()

        win.mainloop()
