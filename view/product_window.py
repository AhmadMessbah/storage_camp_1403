from tkinter import *
import tkinter.ttk as ttk


class Table:
    def refresh_table(self, data_list):
        for item in self.table.get_children():
            self.table.delete(item)

        if data_list:
            for data in data_list:
                self.table.insert("", END, values=data)

    def select(self, event):
        selected = self.table.item(self.table.focus())["values"]
        self.click(selected)

    def __init__(self, master, data_list, headings, widths, x, y, click):
        self.click = click
        columns = list(range(len(headings)))

        self.table = ttk.Treeview(master, columns=columns, show="headings")
        for col in columns:
            self.table.heading(col, text=headings[col])
            self.table.column(col, width=widths[col])

        if data_list:
            for data in data_list:
                self.table.insert("", END, values=data)

        self.table.bind("<ButtonRelease>", self.select)
        self.table.bind("<KeyRelease>", self.select)
        self.table.place(x=x, y=y)


def insert_data():
    pass


root = Tk()
root.title("Stuff")

root.geometry("350x350")

label_name = Label(root, text="name:", font=("Arial", 14))
label_name.grid(row=0, column=0, pady=10, padx=10)
entry_name = Entry(root, font=("Arial", 14))
entry_name.grid(row=0, column=1, pady=10, padx=10)

label_brand = Label(root, text="brand:", font=("Arial", 14))
label_brand.grid(row=5, column=0, pady=10, padx=10)
entry_brand = Entry(root, font=("Arial", 14))
entry_brand.grid(row=5, column=1, pady=10, padx=10)

label_count = Label(root, text="count:", font=("Arial", 14))
label_count.grid(row=2, column=0, pady=10, padx=10)
entry_count = Entry(root, font=("Arial", 14))
entry_count.grid(row=2, column=1, pady=10, padx=10)

label_price_b = Label(root, text="price_b:", font=("Arial", 14))
label_price_b.grid(row=3, column=0, pady=10, padx=10)
entry_price_b = Entry(root, font=("Arial", 14))
entry_price_b.grid(row=3, column=1, pady=10, padx=10)

label_price_b = Label(root, text="price_b:", font=("Arial", 14))
label_price_b.grid(row=4, column=0, pady=10, padx=10)
entry_price_b = Entry(root, font=("Arial", 14))
entry_price_b.grid(row=4, column=1, pady=10, padx=10)

button_insert = Button(root, text="INSERT", command=insert_data, font=("Arial", 20))
button_insert.grid(row=6, column=1, columnspan=2, pady=20)

root.mainloop()
