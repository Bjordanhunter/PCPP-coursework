import tkinter as tk
from tkinter import messagebox as mbox

def aboutApp():
    mbox.showinfo("app", "empty app for menu pratice")

def quitCheck(event=None):
    if mbox.askyesno("", "are you sure you want to quit?"):
        window.destroy()

def openFile():
    mbox.showinfo("opne doc", "opening doc...\n(placeholder)")
    
def fullscreen():
    if not window.attributes("-fullscreen"):
        window.attributes("-fullscreen", True)
    else:
        window.attributes("-fullscreen", False)



window = tk.Tk()

mainMenu = tk.Menu(window)
window.config(menu=mainMenu)

#file menu
subMenu_file = tk.Menu(mainMenu, tearoff=1)
mainMenu.add_cascade(label = "file", menu=subMenu_file, underline=0)
subMenu_file.add_command(label="Open", underline=0, command=openFile)

#open recent submenu
subSubMenu_recent = tk.Menu(subMenu_file, tearoff=0)
subMenu_file.add_cascade(label="open recent", menu=subSubMenu_recent, underline=5)
for i in range(8):
    number = i + 1
    subSubMenu_recent.add_command(label=f"{number}. file_{i}.txt", underline=0)
#recent submenu end

subMenu_file.add_separator()
subMenu_file.add_command(label="quit", command=quitCheck, underline=0, accelerator="Ctrl+Q")


#view menu
subMenu_view = tk.Menu(mainMenu, tearoff=0)
subMenu_view.add_command(label="fullscreen (toggle)", command=fullscreen, underline=0)
mainMenu.add_cascade(label="view", menu=subMenu_view, underline=0)

#about
subMenu_about = tk.Menu(mainMenu)
mainMenu.add_command(label="about", command=aboutApp, underline=3)

window.bind_all("<Control-q>", quitCheck)
window.mainloop()
