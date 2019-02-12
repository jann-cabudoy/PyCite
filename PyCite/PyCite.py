from tkinter import *
from tkinter import ttk


#Main window set up
defaultWidth = 640
defaultHeight = 640

root = Tk()
root.title("PyCite")
mainWindow = ttk.Frame(master=root, width=defaultWidth, height=defaultHeight)
mainWindow.pack()
mainWindow.pack_propagate(0)
root.mainloop()