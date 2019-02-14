from tkinter import *
from tkinter import ttk
from Book import BookCitation
from Stack import Stack

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
object_list = []
textbox = Text(content)
textbox.grid(column=3, row=0)
#StringVar() -> BookCitation
#Takes inputs from Entry and puts as params of a BookCitation
def NewBookCitation():
    new_book = BookCitation(ln, fn, title, pd, pub, city, state)
    object_list.append(new_book)
    return;
#BookCitation -> String
#Takes parameters of BookCitation and outputs into a formatted String
def OutputCitation():
    NewBookCitation()
    a = object_list[0]
    lno = a.getauthlast()
    fno = a.getauthfirst()
    pdo = a.getpubyear()
    titleo = a.gettitle()
    cityo = a.getcity()
    stateo = a.getstate()
    pubo = a.getpub()
    citation_string = lno + ", " + fno[0:1] + "." + " (" + pdo + ") " + titleo + ". " + cityo + ", " + stateo + ": " + pubo + "." + "\n"
    textbox.insert(END, citation_string)
    return;

book_test_button = ttk.Button(content, text="Make New Book Citation", command=OutputCitation)
book_test_button.grid(column = 0, row=7, padx =2 , pady =2)


root.mainloop()