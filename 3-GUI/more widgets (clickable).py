import tkinter as tk
from tkinter import messagebox as mbox
window = tk.Tk()

def switch():
    if button_1.cget('state') == tk.DISABLED:
        button_1.config(state=tk.NORMAL)
        button_1.flash()
    else:
        button_1.flash()
        button_1.config(state=tk.DISABLED)

def mouseover(ev):
    button_1['bg'] = 'green'

def mouseout(ev):
    button_1['bg'] = 'red'

button_1 = tk.Button(window, text="Enabled", bg="red")
button_1.bind("<Enter>", mouseover)
button_1.bind("q", mouseout)
button_1.pack()
button_2 = tk.Button(window, text="Enable/Disable", command=switch)
button_2.pack()


sepframe1 = tk.Frame(window, width=120, height=3, bg="black",)
sepframe1.pack()


def count():
    global counter
    counter += 1

def show():
    mbox.showinfo("",f"counter = {str(counter)}, state = {str(switch.get())}")

switch = tk.IntVar()
counter = 0
button_3 = tk.Button(window, text="Show", command=show)
button_3.pack()
checkbutton = tk.Checkbutton(window, text="tick",variable=switch, command=count)
checkbutton.pack()


sepframe2 = tk.Frame(window, width=120, height=3, bg="black",)
sepframe2.pack()


def showradio():
    mbox.showinfo("", f"radio_1= {radio_1_var.get()},radio_2= {radio_2_var.get()}, radio 3 = {radio3_var.get()}")


def command_1():
    radio_2_var.set(radio_1_var.get())


def command_2():
    radio_1_var.set(radio_2_var.get())


button = tk.Button(window, text="Show", command=showradio)
button.pack()

radio_1_var = tk.IntVar()
radio_1_1 = tk.Radiobutton(window, text="pizza", variable=radio_1_var, value=1, command=command_1)
radio_1_1.select()
radio_1_1.pack()
radio_1_2 = tk.Radiobutton(window, text="burger", variable=radio_1_var, value=2, command=command_1)
radio_1_2.pack()

radio_2_var = tk.IntVar()
radio_2_1 = tk.Radiobutton(window, text="FR", variable=radio_2_var, value=2, command=command_2)
radio_2_1.pack()
radio_2_2 = tk.Radiobutton(window, text="IT", variable=radio_2_var, value=1, command=command_2)
radio_2_2.select()
radio_2_2.pack()

radio3_var = tk.IntVar()
radio3_1 = tk.Radiobutton(window, text="option: 1", variable=radio3_var, value=1)
radio3_1.pack()
radio3_2 = tk.Radiobutton(window, text="option: 2", variable=radio3_var, value=2)
radio3_2.pack()
radio3_3 = tk.Radiobutton(window, text="option: 3", variable=radio3_var, value=3)
radio3_3.pack()

window.mainloop()
