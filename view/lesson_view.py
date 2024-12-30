from view.component.table import Table
from view.component.label_and_entry import LabelAndEntry
from da.product_da import *
from tkinter import *
import tkinter.messagebox as msg

def reset_form():
    id.variable.set(0)
    name.variable.set("")
    quantity.variable.set(0)
    price.variable.set(0)
    table.show_data(find_all())

def save_click():
    try:
        product = Product(None, name.variable.get(), quantity.variable.get(), price.variable.get())
        save(product)
        msg.showinfo("Save", "Save Done")
        reset_form()
    except Exception as e:
        msg.showerror("Save Error", f"Error : {e}")

def edit_click():
    try:
        product = Product(id.variable.get(), name.variable.get(), quantity.variable.get(), price.variable.get())
        edit(product)
        msg.showinfo("Edit", "Edit Done")
        reset_form()
    except Exception as e:
        msg.showerror("Edit Error", f"Error : {e}")

def remove_click():
    if msg.askyesno("Confirm Remove", "Are you sure you want to remove this product?"):
        try:
            product = Product(id.variable.get(), name.variable.get(), quantity.variable.get(), price.variable.get())
            save(product)
            msg.showinfo("Remove", "Remove Done")
            reset_form()
        except Exception as e:
            msg.showerror("Remove Error", f"Error : {e}")


win = Tk()
win.geometry("570x270")
win.title("Product View")

id = LabelAndEntry(win, "ID",20,20, state="readonly", data_type="int")
name = LabelAndEntry(win, "Name",20,60)
quantity = LabelAndEntry(win, "Quantity",20,100, data_type="int")
price = LabelAndEntry(win, "Price",20,140, data_type="int")

table = Table(win, ["Id", "Name", "Quantity", "Price"], [50,100,60,80], 250,20)


Button(win, text="Save",width=7, command=save_click).place(x=20, y = 220)
Button(win, text="Edit",width=7, command=edit_click).place(x=92, y = 220)
Button(win, text="Remove",width=7, command=remove_click).place(x=164, y = 220)



win.mainloop()

