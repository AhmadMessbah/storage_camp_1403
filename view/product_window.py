import tkinter.messagebox as msg
from view.components import *
from controller.product_controller import *


class ProductForm:

    def __init__(self):
        win = Tk()
        win.geometry("300x550")

        def product_select(row):
            product_name.variable.set(row[0])
            product_brand.variable.set(row[1])
            product_quantity.variable.set(row[2])
            product_buyer_price.variable.set(row[3])
            product_seller_price.variable.set(row[4])

        def product_save_click():

            print('name: ', product_name.get())
            print('brand: ', product_brand.get())
            print('quantity: ', product_quantity.get())

            status, message = save_product(
                product_name.get(),
                product_brand.get(),
                product_quantity.get(),
                product_buyer_price.get(),
                product_seller_price.get()
            )

            if status:
                msg.showinfo("Save", message)
                # refresh_product_side()
            else:
                msg.showerror("Save Error", message)

        def product_edit_click():
            status, message = edit_product(
                product_name.get(),
                product_brand.get(),
                product_quantity.get(),
                product_buyer_price.get(),
                product_seller_price.get()
            )

            if status:
                msg.showinfo("Edit", message)
                # refresh_person_side()
            else:
                msg.showerror("Edit Error", message)

        def product_remove_click():
            status, message = remove_product(product_id.variable.get())

            if status:
                msg.showinfo("Remove", message)
                # refresh_person_side()
            else:
                msg.showerror("Remove Error", message)

        # Person
        Label(win, text="Product Info", font=("Arial", 16)).place(x=20, y=10)
        product_name = TextAndLabel(win, "name", 20, 50).get_var()
        product_brand = TextAndLabel(win, "brand", 20, 85).get_var()
        product_quantity = TextAndLabel(win, "quantity", 20, 120).get_var()
        product_buyer_price = TextAndLabel(win, "buyer_price", 20, 155).get_var()
        product_seller_price = TextAndLabel(win, "seller_price", 20, 180).get_var()

        product_table = Table(win,
                        None,
                        ["name", "family", "phone"],
                        [60, 100, 100],
                        20,
                        210,
                        product_select)
        Button(win, text="Saveproduct", width=10, command=product_save_click).place(x=20, y=470)
        Button(win, text="EditProduct", width=10, command=product_edit_click).place(x=110, y=470)
        Button(win, text="Removeproduct", width=10, command=product_remove_click).place(x=200, y=470)

        # refresh_person_side()

        win.mainloop()
