import tkinter as tk
from tkinter import messagebox as mbox

def close():
    replay = mbox.askquestion("Quit?","Are you sure?")
    if replay == "yes":
        skylight.destroy()

skylight = tk.Tk()
skylight.title("skylight")
button = tk.Button(skylight, text="Bye", command=close)
button.place(x=10,y=10)
skylight.mainloop()
