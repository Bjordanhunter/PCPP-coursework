import tkinter as tk

def blink():
    global isWhite
    if isWhite:
        colour = "black"
    else:
        colour = "white"

    isWhite = not isWhite
    frame["bg"] = colour
    frame.after(500,blink)

def remove():
    frame.destroy()

def flip_focus():
    if window.focus_get() is button1:
        button2.focus_set()
    else:
        button1.focus_set()
    window.after(1000,flip_focus)

isWhite = True
window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg="white")
frameButton = tk.Button(frame,text="im in frame")
frameButton.place(x=10,y=10)
frame.after(500,blink)
frame.pack()
frame.after(5000,remove)

button1 = tk.Button(window, text="one", highlightcolor="blue", highlightthickness=10)
button2 = tk.Button(window, text="two", highlightcolor="blue")
button1.pack()
button2.pack()
window.after(1000, flip_focus)


window.mainloop()
