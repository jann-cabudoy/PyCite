from tkinter import *
from tkinter import ttk
from citationdeps import Book

#Main window set up
root = Tk()
root.title("PyCite")

content = ttk.Frame(root, padding="3 3 12 12")

fn = StringVar()
ln = StringVar()
pd = StringVar()
city = StringVar()
state = StringVar()
pub = StringVar()
title = StringVar()

first_name = ttk.Entry(content, textvariable=fn)
last_name = ttk.Entry(content, textvariable=ln)
pub_date = ttk.Entry(content, textvariable=pd)
city = ttk.Entry(content, textvariable=city)
state = ttk.Entry(content, textvariable=state)
publisher = ttk.Entry(content, textvariable=pub)
title = ttk.Entry(content, textvariable=title)

fn_tag = ttk.Label(content, text="Author First Name")
ln_tag = ttk.Label(content, text="Author Last Name")
pd_tag = ttk.Label(content, text="Pub. Date")
city_tag = ttk.Label(content, text="City")
state_tag = ttk.Label(content, text="State")
pub_tag = ttk.Label(content, text="Publisher")
title_tag = ttk.Label(content, text="Title")

content.grid(column=0, row=0, sticky=E)
fn_tag.grid(column=0, row=0, sticky=E)
ln_tag.grid(column=0, row=1, sticky=E)
pd_tag.grid(column=0, row=2, sticky=E)
city_tag.grid(column=0, row=3, sticky=E)
state_tag.grid(column=0, row=4, sticky=E)
pub_tag.grid(column=0, row=5, sticky=E)
title_tag.grid(column=0, row=6, sticky=E)

first_name.grid(column=1, row=0, padx=2, pady=2)
last_name.grid(column=1, row=1, padx=2, pady=2)
pub_date.grid(column=1, row=2, padx=2, pady=2)
city.grid(column=1, row=3, padx=2, pady=2)
state.grid(column=1, row=4, padx=2, pady=2)
publisher.grid(column=1, row=5, padx=2, pady=2)
title.grid(column=1, row=6, padx=2, pady=2)
#Testing book class
def NewBookCitation():
    new_book = BookCitation(ln, fn, title, pd, pub, city, state)
    return new_book;

book_test_button = ttk.Button(content, text="Make New Book Citation", command=NewBookCitation)

root.mainloop()