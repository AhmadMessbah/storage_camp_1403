import tkinter.messagebox as msg
from view.components import *
from controller.person_controller import *


class PersonForm:

    def __init__(self):
        win = Toplevel()
        win.title("Person Form")
        win.geometry("450x500")

        def refresh_person_side():
            person_id.variable.set("")
            person_name.variable.set("")
            person_family.variable.set("")
            person_phone.variable.set("")
            person_table.refresh_table(find_all()[1] if find_all()[0] else None)

        def person_select(row):
            person_id.variable.set(row[0])
            person_name.variable.set(row[1])
            person_family.variable.set(row[2])
            person_phone.variable.set(row[3])

        def person_save_click():
            status, message = save_person(
                person_name.variable.get(),
                person_family.variable.get(),
                person_phone.variable.get())

            if status:
                msg.showinfo("Save", message)
                refresh_person_side()
            else:
                msg.showerror("Save Error", message)

        def person_edit_click():
            status, message = edit_person(
                person_id.variable.get(),
                person_name.variable.get(),
                person_family.variable.get(),
                person_phone.variable.get())

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

        Label(win, text="Person Info", font=("Arial", 16)).place(x=20, y=10)
        person_id = TextAndLabel(win, "id", 20, 50, state="readonly")
        person_name = TextAndLabel(win, "name", 20, 85)
        person_family = TextAndLabel(win, "family", 20, 120)
        person_phone = TextAndLabel(win, "phone", 20, 155)

        person_table = Table(win,
                             None,
                             ["id", "name", "family", "phone"],
                             [60, 100, 100, 150],
                             20,
                             190,
                             person_select)
        refresh_person_side()
        Button(win, text="Save Person", width=12, command=person_save_click).place(x=60, y=450)
        Button(win, text="Edit Person", width=12, command=person_edit_click).place(x=180, y=450)
        Button(win, text="Remove Person", width=12, command=person_remove_click).place(x=300, y=450)
        # Button(win, text="Home", width=12, command="open_home_page").place(x=300, y=450)

        win.mainloop()
