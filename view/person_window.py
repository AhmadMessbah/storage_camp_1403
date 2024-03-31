import tkinter.messagebox as msg
from view.components import *
from controller.person_controller import *


class PersonForm:

    def __init__(self):
        win = Tk()
        win.geometry("300x450")

        def person_select(row):
            person_id.variable.set(row[0])
            person_name.variable.set(row[1])
            person_family.variable.set(row[2])

        def person_save_click():
            status, message = save_person(
                person_name.variable.get(),
                person_family.variable.get())

            if status:
                msg.showinfo("Save", message)
                refresh_person_side()
            else:
                msg.showerror("Save Error", message)

        def person_edit_click():
            status, message = edit_person(
                person_id.variable.get(),
                person_name.variable.get(),
                person_family.variable.get())

            if status:
                msg.showinfo("Edit", message)
                refresh_person_side()
            else:
                msg.showerror("Edit Error", message)

        def person_remove_click():
            status, message = remove_person(person_id.variable.get())

            if status:
                msg.showinfo("Remove", message)
                refresh_person_side()
            else:
                msg.showerror("Remove Error", message)

        # Person
        Label(win, text="Person Info", font=("Arial", 16)).place(x=20, y=10)
        person_id = TextAndLabel(win, "name", 20, 50)
        person_name = TextAndLabel(win, "family", 20, 85)
        person_family = TextAndLabel(win, "phone", 20, 120)

        p_table = Table(win,
                        None,
                        ["name", "family", "phone"],
                        [60, 100, 100],
                        20,
                        150,
                        person_select)

        Button(win, text="Save Person", width=11, command=person_save_click).place(x=20, y=400)
        Button(win, text="Edit Person", width=11, command=person_edit_click).place(x=110, y=400)
        Button(win, text="Remove Person", width=11, command=person_remove_click).place(x=200, y=400)

        # refresh_person_side()

        win.mainloop()
