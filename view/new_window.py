import tkinter as tk


def open_person(title):
    # person = tk.Toplevel()
    # person.title(title)
    # person.title("Person")
    def insert_data():
        pass


    root = tk.Tk()
    root.title("person")

    root.geometry("700x300")

    label_id = tk.Label(root, text="ID:", font=("Arial", 14))
    label_id.grid(row=0, column=0, pady=10, padx=10)
    entry_id = tk.Entry(root, font=("Arial", 14))
    entry_id.grid(row=0, column=1, pady=10, padx=10)

    label_name = tk.Label(root, text="Name:", font=("Arial", 14))
    label_name.grid(row=0, column=2, pady=10, padx=10)
    entry_name = tk.Entry(root, font=("Arial", 14))
    entry_name.grid(row=0, column=3, pady=10, padx=10)

    label_family = tk.Label(root, text="Family:", font=("Arial", 14))
    label_family.grid(row=2, column=0, pady=10, padx=10)
    entry_family = tk.Entry(root, font=("Arial", 14))
    entry_family.grid(row=2, column=1, pady=10, padx=10)

    label_phone = tk.Label(root, text="Phone:", font=("Arial", 14))
    label_phone.grid(row=3, column=0, pady=10, padx=10)
    entry_phone = tk.Entry(root, font=("Arial", 14))
    entry_phone.grid(row=3, column=1, pady=10, padx=10)

    button_insert = tk.Button(root, text="INSERT", command=insert_data, font=("Arial", 14))
    button_insert.grid(row=6, column=2, columnspan=2, pady=20)

    root.mainloop()

    return open_stuff()

def open_stuff(title):
    # open_stuff = tk.Toplevel()
    # open_stuff.title(title)
    # open_stuff.title("Stuff")
    import tkinter as tk
    from tkinter import ttk

    class Table:
        def __init__(self, master):
            self.table = ttk.Treeview(master, columns=("Name", "Brand", "Count", "Price Bought"), show="headings")
            self.table.heading("Name", text="Name")
            self.table.heading("Brand", text="Brand")
            self.table.heading("Count", text="Count")
            self.table.heading("Price Bought", text="Price Bought")
            self.table.grid(row=7, column=0, columnspan=4)

        def insert_data(self, name, brand, count, price_b):
            self.table.insert("", tk.END, values=(name, brand, count, price_b))

    root = tk.Tk()
    root.title("Stuff")
    root.geometry("850x500")

    table = Table(root)

    label_name = tk.Label(root, text="Name:", font=("Arial", 14))
    label_name.grid(row=0, column=0)
    entry_name = tk.Entry(root, font=("Arial", 14))
    entry_name.grid(row=0, column=1)

    label_brand = tk.Label(root, text="Brand:", font=("Arial", 14))
    label_brand.grid(row=1, column=0)
    entry_brand = tk.Entry(root, font=("Arial", 14))
    entry_brand.grid(row=1, column=1)

    label_count = tk.Label(root, text="Count:", font=("Arial", 14))
    label_count.grid(row=2, column=0)
    entry_count = tk.Entry(root, font=("Arial", 14))
    entry_count.grid(row=2, column=1)

    label_price_b = tk.Label(root, text="Price Bought:", font=("Arial", 14))
    label_price_b.grid(row=3, column=0)
    entry_price_b = tk.Entry(root, font=("Arial", 14))
    entry_price_b.grid(row=3, column=1)

    def insert_data():
        name = entry_name.get()
        brand = entry_brand.get()
        count = entry_count.get()
        price_b = entry_price_b.get()
        table.insert_data(name, brand, count, price_b)

    button_insert = tk.Button(root, text="INSERT", command=insert_data, font=("Arial", 20))
    button_insert.grid(row=4, column=0, columnspan=2)

    root.mainloop()

    return open_stuff

def open_transaction(title):
    open_transaction = tk.Toplevel()
    open_transaction.title(title)
    open_transaction.title("Transaction")
    return open_transaction

def create_new_window(title, win):
    if title == "Person":
        open_person(title)
    elif title == "Stuff":
        open_stuff(title)
    elif title == "Transaction":
        open_transaction(title)

def create_button(name, win):
    def on_button_click():
        create_new_window(name, win)
    return on_button_click
