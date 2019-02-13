from tkinter import *
from tkinter import ttk
class ApplicationWindow():
    """Main Application Window"""

    def __init__(self):
        root = Tk()
        root.title("PyCite")

        content = ttk.Frame(root, padding="3 3 12 12")

        fn = StringVar()
        ln = StringVar()
        pd = StringVar()
        city = StringVar()
        state = StringVar()
        pub = StringVar()

        first_name = ttk.Entry(content, textvariable=fn)
        last_name = ttk.Entry(content, textvariable=ln)
        pub_date = ttk.Entry(content, textvariable=pd)
        city = ttk.Entry(content, textvariable=city)
        state = ttk.Entry(content, textvariable=state)
        publisher = ttk.Entry(content, textvariable=pub)

        fn_tag = ttk.Label(content, text="Author First Name")
        ln_tag = ttk.Label(content, text="Author Last Name")
        pd_tag = ttk.Label(content, text="Pub. Date")
        city_tag = ttk.Label(content, text="City")
        state_tag = ttk.Label(content, text="State")
        pub_tag = ttk.Label(content, text="Publisher")

        create_citation = ttk.Button(content, text="Create Citation")

        content.grid(column=0, row=0, sticky=E)
        fn_tag.grid(column=0, row=0, sticky=E)
        ln_tag.grid(column=0, row=1, sticky=E)
        pd_tag.grid(column=0, row=2, sticky=E)
        city_tag.grid(column=0, row=3, sticky=E)
        state_tag.grid(column=0, row=4, sticky=E)
        pub_tag.grid(column=0, row=5, sticky=E)

        first_name.grid(column=1, row=0, padx=2, pady=2)
        last_name.grid(column=1, row=1, padx=2, pady=2)
        pub_date.grid(column=1, row=2, padx=2, pady=2)
        city.grid(column=1, row=3, padx=2, pady=2)
        state.grid(column=1, row=4, padx=2, pady=2)
        publisher.grid(column=1, row=5, padx=2, pady=2)

        root.mainloop()

    

