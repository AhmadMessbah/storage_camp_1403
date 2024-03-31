import tkinter.messagebox as msg
from view.components import *
from controller.product_controller import *


class ProductForm:

    def __init__(self):
        win = Tk()
        win.geometry("300x450")

        def product_select(row):
            product_id.variable.set(row[0])
            product_name.variable.set(row[1])
            product_family.variable.set(row[2])

        def product_save_click():
            status, message = save_product(
                product_name.variable.get(),
                product_family.variable.get())

            if status:
                msg.showinfo("Save", message)
                refresh_product_side()
            else:
                msg.showerror("Save Error", message)

        def product_edit_click():
            status, message = edit_product(
                product_id.variable.get(),
                product_name.variable.get(),
                product_family.variable.get())

            if status:
                msg.showinfo("Edit", message)
                refresh_person_side()
            else:
                msg.showerror("Edit Error", message)

        def product_remove_click():
            status, message = remove_product(product_id.variable.get())

            if status:
                msg.showinfo("Remove", message)
                refresh_person_side()
            else:
                msg.showerror("Remove Error", message)

        # Person
        Label(win, text="Product Info", font=("Arial", 16)).place(x=20, y=10)
        product_id = TextAndLabel(win, "name", 20, 50)
        product_name = TextAndLabel(win, "family", 20, 85)
        product_family = TextAndLabel(win, "phone", 20, 120)

        product_table = Table(win,
                        None,
                        ["name", "family", "phone"],
                        [60, 100, 100],
                        20,
                        150,
                        product_select)
        Button(win, text="SavePerson", width=10, command=product_save_click).place(x=20, y=400)
        Button(win, text="EditPerson", width=10, command=product_edit_click).place(x=110, y=400)
        Button(win, text="RemovePerson", width=10, command=product_remove_click).place(x=200, y=400)

        # refresh_person_side()

        win.mainloop()
