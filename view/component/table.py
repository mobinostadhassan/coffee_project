import tkinter.ttk as ttk
from tkinter import *

class Table:
    def __init__(self, window, headings, widths,x,  y):
        columns = list(range(len(headings)))

        self.table = ttk.Treeview(window, columns=columns, show="headings")

        for i in columns:
            self.table.heading(i, text=headings[i])
            self.table.column(i, width=widths[i])

        self.table.place(x=x, y=y)

    def clear_table(self):
        for item in self.table.get_children():
            self.table.delete(item)


    def show_data(self, data_list):
        self.clear_table()
        for item in data_list:
            self.table.insert("", END, values=item.to_tuple())