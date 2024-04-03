from tkinter import *
import tkinter.ttk as ttk
from typing import Literal


class Table:

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
        # self.table.bind("<KeyRelease>", self.select)
        self.table.place(x=x, y=y)

    def refresh_table(self, data_list):
        for item in self.table.get_children():
            self.table.delete(item)

        if data_list:
            for data in data_list:
                self.table.insert("", END, values=data)

    def select(self, event):
        selected = self.table.item(self.table.focus())["values"]
        self.click(selected)


class TextAndLabel:
    def __init__(self, master, text, x, y, distance=80, state: Literal["normal", "disabled", "readonly"] = "normal"):
        Label(master, text=text).place(x=x, y=y)
        self.variable = StringVar()
        Entry(master, textvariable=self.variable, state=state).place(x=x + distance, y=y)
        # self.var.place(x=x + distance, y=y)

    # def get_var(self):
    #     return self.var


