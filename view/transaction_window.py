import tkinter.messagebox as msg
from view.components import *
from controller.product_controller import *


class TransactionForm:

    def __init__(self):
        win = Toplevel()
        win.geometry("700x550")
        win.title("Product Form")

        def refresh_transaction_table():
            pass

        def product_select(row):
            pass

        def product_save_click():
            pass

        def product_edit_click():
            pass

        def product_remove_click():
            pass

        Label(win, text="Transaction Info", font=("Arial", 16)).place(x=20, y=10)

        transaction_table = Table(win,
                                  None,
                                  ["id", "name", "brand", "quantity", "buyer price", "seller price"],
                                  [60, 100, 100, 100, 150, 150],
                                  20,
                                  260,
                                  product_select)
        Button(win, text="Save product", width=12, command=product_save_click).place(x=100, y=500)
        Button(win, text="Edit Product", width=12, command=product_edit_click).place(x=300, y=500)
        Button(win, text="Remove product", width=12, command=product_remove_click).place(x=500, y=500)

        refresh_transaction_table()

        win.mainloop()
