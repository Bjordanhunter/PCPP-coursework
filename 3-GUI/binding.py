##import tkinter as tk
##from tkinter import messagebox as mbox
##
##def showInfoBox(event=None):
##    if event is None:
##        mbox.showinfo("info box","this is\nsome info.")
##    else:
##        mbox.showinfo("event info", str(event))
##
##window = tk.Tk()
##
##label = tk.Label(window, text="Label")
##label.bind("<Button-1>", showInfoBox)
##label.pack()
##
##button_1 = tk.Button(window, text="Show info", command=showInfoBox)
##button_1.pack()
##
##frame = tk.Frame(window, height=30, width=100, bg="pink")
##frame.bind("<Button-1>", showInfoBox)
##frame.pack()
##
##button_2 = tk.Button(window, text="Quit", command=window.destroy)
##button_2.pack()
##
##window.mainloop()

import tkinter as tk


def on_off():
    global switch
    if switch:
        label.unbind("<Button-1>")
        button.config(bg="red")
    else:
        label.bind("<Button-1>", rhyme)
        button.config(bg="light green")
    switch = not switch


def rhyme(dummy):
    global word_no, words
    word_no += 1
    label.config(text=words[word_no % len(words)])
    print(vars(dummy))


switch = True
words = ["Old", "McDonald", "Had", "A", "Farm"]
word_no = 0
window = tk.Tk()
button = tk.Button(window, text="On/Off", command=on_off, bg="light green")
button.pack()
label = tk.Label(window, text=words[0])
label.bind("<Button-1>", rhyme)
label.pack()
window.mainloop()
