import tkinter as tk
from tkinter import*


#Window is our Main frame of input and output system
window = tk.Tk()
window.title("game of life input and output screen")

window.configure(background='snow')

def printValue():
    cname = cells_entry.get()
    Label(window, text=f'{cname} cells appended to grid', pady=20, bg='#ffbf00').pack()


lb1 = tk.Label(window, text="enter a number in the multipes of 20 utmost 100 to append to grid",pady=20, bg='deep pink').pack()
cells_entry = Entry(window)
cells_entry.place(x=200, y=310)
cells_entry.pack(pady=30)

Button(window,text="Click to add cells", padx=10, pady=5,command=printValue).pack()

def printValue1():
    cname1 = cells_entry1.get()
    Label(window, text=f'searching cell {cname1}', pady=20, bg='blue').pack()

lb2 = tk.Label(window, text="searching a cell for its state", width=20, height=1, fg="black", bg="deep pink", font=('times', 20, ' bold ')) 
cells_entry1 = Entry(window)
cells_entry1.place(x=400, y=310)
cells_entry1.pack(pady=30)

Button(window,text="Enter searching cell", padx=10, pady=5,command=printValue1).pack()

window.mainloop()
