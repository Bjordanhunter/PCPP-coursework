import tkinter as tk

#cursors: https://www.tcl.tk/man/tcl8.4/TkCmd/cursors.htm

def onOff():
    global button
##    state = button["text"]
    state = button.cget("text")
    if state == "ON":
        state = "OFF"
        bg = "red"
        cursor = "trek"
    else:
        state = "ON"
        bg = "light green"
        cursor = "shuttle"
##    button["text"] = state
##    button["bg"] = bg
    button.config(text=state)
    button.config(bg=bg)
    button.config(cursor=cursor)

window = tk.Tk()

button = tk.Button(window, text="OFF", command=onOff, bg="red", activebackground="dark gray")
button.grid(column=0,row=0)
button["borderwidth"] = 0
button["highlightthickness"] = 10
button["padx"] = 5
button["pady"] = 5
button["underline"] = 0
button["wraplength"] = -1
button["width"] = 10
button["height"] = 1
button["disabledforeground"] = "blue"
button["anchor"] = "nw"


label_1 = tk.Label(window, text="Quick brown fox jumps over the lazy dog",
                   cursor="shuttle")
label_1.grid(column=0, row=1)
label_2 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Times", "12"),
                   cursor="trek")
label_2.grid(column=0, row=2)
label_3 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Arial", "16", "bold"),
                   cursor="rtl_logo")
label_3.grid(column=0, row=3)

window.mainloop()
