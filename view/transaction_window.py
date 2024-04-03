import tkinter.messagebox as msg
from view.components import *
from controller.product_controller import *


class ProductForm:

    def __init__(self):
        win = Toplevel()
        win.geometry("700x550")
        win.title("Product Form")

        def refresh_transaction_table():
            product_id.variable.set("")
            product_name.variable.set("")
            product_brand.variable.set("")
            product_quantity.variable.set(int())
            product_buyer_price.variable.set(int())
            product_seller_price.variable.set(int())
            product_table.refresh_table(find_all()[1] if find_all()[0] else None)

        def product_select(row):
            product_id.variable.set(row[0])
            product_name.variable.set(row[1])
            product_brand.variable.set(row[2])
            product_quantity.variable.set(row[3])
            product_buyer_price.variable.set(row[4])
            product_seller_price.variable.set(row[5])

        def product_save_click():

            status, message = save_product(
                product_name.variable.get(),
                product_brand.variable.get(),
                product_quantity.variable.get(),
                product_buyer_price.variable.get(),
                product_seller_price.variable.get()
            )

            if status:
                msg.showinfo("Save", message)
                refresh_product_side()
            else:
                msg.showerror("Save Error", message)

        def product_edit_click():
            status, message = edit_product(
                product_id.variable.get(),
                product_name.variable.get(),
                product_brand.variable.get(),
                product_quantity.variable.get(),
                product_buyer_price.variable.get(),
                product_seller_price.variable.get()
            )

            if status:
                msg.showinfo("Edit", message)
                refresh_product_side()
            else:
                msg.showerror("Edit Error", message)

        def product_remove_click():
            status, message = remove_product(product_id.variable.get())

            if status:
                msg.showinfo("Remove", message)
                refresh_product_side()
            else:
                msg.showerror("Remove Error", message)

        Label(win, text="Product Info", font=("Arial", 16)).place(x=20, y=10)
        product_id = TextAndLabel(win, "id", 20, 50, state="readonly")
        product_name = TextAndLabel(win, "name", 20, 85)
        product_brand = TextAndLabel(win, "brand", 20, 120)
        product_quantity = TextAndLabel(win, "quantity", 20, 155)
        product_buyer_price = TextAndLabel(win, "buyer price", 20, 190)
        product_seller_price = TextAndLabel(win, "seller price", 20, 225)

        product_table = Table(win,
                              None,
                              ["id", "name", "brand", "quantity", "buyer price", "seller price"],
                              [60, 100, 100, 100, 150, 150],
                              20,
                              260,
                              product_select)
        Button(win, text="Save product", width=12, command=product_save_click).place(x=100, y=500)
        Button(win, text="Edit Product", width=12, command=product_edit_click).place(x=300, y=500)
        Button(win, text="Remove product", width=12, command=product_remove_click).place(x=500, y=500)

        refresh_product_side()

        win.mainloop()

