import tkinter as tk

window1 = tk.Tk()
window1.title("window 1 - place")
button_1 = tk.Button(window1, text="Button #1")
button_2 = tk.Button(window1, text="Button #2")
button_3 = tk.Button(window1, text="Button #3")
button_1.place(x=10, y=10, width=150)
button_2.place(x=20, y=40)
button_3.place(x=30, y=70, height=50)


window2 = tk.Tk()
window2.title("window 2 - grid")
button_1 = tk.Button(window2, text="Button #1")
button_2 = tk.Button(window2, text="Button #2")
button_3 = tk.Button(window2, text="Button #3")
button_1.grid(row=0, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=2, column=0, columnspan=2)


window3 = tk.Tk()
window3.title("window 3 - pack")
button_1 = tk.Button(window3, text="Button #1")
button_2 = tk.Button(window3, text="Button #2")
button_3 = tk.Button(window3, text="Button #3")
button_1.pack(side=tk.RIGHT, fill=tk.Y)
button_2.pack(side="top")
button_3.pack()
window3.mainloop()
window1.mainloop()
window2.mainloop()
