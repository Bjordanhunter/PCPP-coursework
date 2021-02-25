import tkinter as tk


def digits_only(*args):
    global last_string
    string = text.get()
    if string == '' or string.isdigit():  # Field's content is valid.
        last_string = string
    else:
        text.set(last_string)
    print(string)

last_string = ''
window = tk.Tk()
text = tk.StringVar()
entry = tk.Entry(window, textvariable=text)
text.set(last_string)
text.trace('w', digits_only) # how it calls the function
entry.pack()
entry.focus_set()
window.mainloop()
