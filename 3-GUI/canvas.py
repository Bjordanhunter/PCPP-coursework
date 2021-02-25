import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg="light blue")
canvas.create_line(0,0, 400,400)#, 90,90, 10,90, 
            #fill="red", smooth=True, arrow=tk.BOTH)

canvas.create_rectangle(110,10, 190,90, outline="hot pink", 
            fill="blue", width=5)

canvas.create_polygon(210,45, 250,10, 290,45, 270,90, 230,90,
            outline="blue", fill="red", width=3)

canvas.create_oval(310,10, 390,90, width=4, outline="yellow",
            fill="pink")

canvas.create_arc(-50,110, 90,240, outline="red", width=3,
            style=tk.PIESLICE, fill="blue" )

canvas.create_arc(110,110, 190,190, outline='blue', width=5,
            style=tk.CHORD, start=80, fill='white')

canvas.create_arc(210,110, 310,190, outline='green', width=5,
            style="ARCa", start=90, extent=135)

canvas.create_text(350,150, text="this is some\nsample text",
            font=("Arial","12","bold"), justify=tk.CENTER,
            fill='white')

image = ImageTk.PhotoImage(Image.open("logo.png").resize((80,80)))
canvas.create_image(50,250, image=image)

button = tk.Button(window, text="quit",command=window.destroy).f
canvas.grid(row=0)
button.grid(row=1)

window.mainloop()