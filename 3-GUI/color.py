import tkinter as tk

#color list: http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm

window = tk.Tk()
button1 = tk.Button(window, text="Button #1", bg="red", foreground="blue",
                    activebackground="yellow", activeforeground="hotpink")
button2 = tk.Button(window, text="button #2", bg="#FF00FF", fg="#00ff00",
                    activebackground="#00ff00", activeforeground="#ff00ff")
button1.pack()
button2.pack()
window.mainloop()
