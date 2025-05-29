from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from file_manager import *
from financial import Financial

financial_list = read_from_file("financials.dat")


def load_data(financial_list):
    financial_list = read_from_file("financials.dat")
    for row in table.get_children():
        table.delete(row)

    for financial in financial_list:
        table.insert("", END, values=financial.to_tuple())


def reset_form():
    id.set(len(financial_list) + 1)
    amount.set(0)
    date_time.set("")
    document_type.set("pay")
    description.set("")
    load_data(financial_list)


def save_btn_click():
    financial = Financial(id.get(), amount.get(), date_time.get(), document_type.get(), description.get())
    errors = financial.validator()

    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "Financial document saved")
        financial_list.append(financial)
        write_to_file("financials.dat", financial_list)
        reset_form()


def table_select(x):
    selected_financial = table.item(table.focus())["values"]
    if selected_financial:
        id.set(selected_financial[0])
        amount.set(selected_financial[1])
        date_time.set(selected_financial[2])
        document_type.set(selected_financial[3])
        description.set(selected_financial[4])


def remove_selected():
    selected_item = table.focus()
    if selected_item:
        table.delete(selected_item)


def edit_btn_click():
    # Implement edit functionality here
    pass


def remove_btn_click():
    remove_selected()  # Call the function to remove the selected item


window = Tk()
window.title("Financial Info")
window.geometry("610x350")

# Id
Label(window, text="Id").place(x=20, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=80, y=20)

# Amount
Label(window, text="Amount").place(x=20, y=60)
amount = IntVar()
Entry(window, textvariable=amount).place(x=80, y=60)

# Date Time
Label(window, text="Date Time").place(x=20, y=100)
date_time = StringVar()
Entry(window, textvariable=date_time).place(x=80, y=100)

# Document Type
Label(window, text="Document Type").place(x=20, y=140)
document_type = StringVar(value="pay")
OptionMenu(window, document_type, "pay", "receive").place(x=150, y=140)  # Corrected "pa" to "pay"

# Description
Label(window, text="Description").place(x=19, y=180)
description = StringVar()
Entry(window, textvariable=description).place(x=80, y=180)

table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5], show="headings")
table.heading(1, text="Id")
table.heading(2, text="Amount")
table.heading(3, text="Date Time")
table.heading(4, text="Document Type")
table.heading(5, text="Description")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=150)

table.bind("<<TreeviewSelect>>", table_select)

table.place(x=230, y=20)

Button(window, text="Save", width=6, command=save_btn_click).place(x=20, y=220)
Button(window, text="Edit", width=6, command=edit_btn_click).place(x=90, y=220)
Button(window, text="Remove", width=6, command=remove_btn_click).place(x=160, y=220)
Button(window, text="Clear", width=6, command=reset_form).place(x=20, y=180, width=190)

reset_form()

window.mainloop()
