import tkinter as tk
from tkinter import messagebox

def decreaseTitle(event=None):
    global counter
    if counter > 0:
        counter -= 1
        window.title(counter)

counter = 10
window = tk.Tk()
window.title(counter)
window.bind("<Button-1>", decreaseTitle)

##window.tk.call("wm", "iconphoto", window._w, tk.PhotoImage(file='logo.png'))
window.iconphoto(False, tk.PhotoImage(file='logo.png'))


def resize(*args):
    global size, grows
    if grows:
        size += 25
        if size > 150:
            grows = False
    else:
        size -= 25
        if size < 100:
            grows = True
    window.geometry(f"{size}x{size}")
    print(size)

size = 50
grows = True
window.geometry("75x75")
window.bind("<Button-3>", resize)


window.minsize(width=75, height=75)
window.maxsize(width=500, height=500)
##window.resizable(width=False, height=False)


def quit_check():
    if messagebox.askyesno("quit?", "are you sure?"):
        window.destroy()

window.protocol("WM_DELETE_WINDOW", quit_check)

msg = tk.Entry(window, text="test").pack()
print(msg)
window.mainloop()
