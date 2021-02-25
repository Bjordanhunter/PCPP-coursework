import tkinter as tk


##label
def toString(x):
    return f"Current counter\nvalue is: {x}"

counter = 0
def increaseCount():
    global counter
    counter += 1
    labelText.set(toString(counter))

window = tk.Tk()
increaseCountButton = tk.Button(window, text="increase count", command=increaseCount)
increaseCountButton.pack()
labelText = tk.StringVar()
label = tk.Label(window, textvariable=labelText)
# labelText.set(toString(counter))
label.pack()


sepframe1 = tk.Frame(window, width=120, height=3, bg="black",)
sepframe1.pack()


##message
def doItAgain():
    messageText.set(messageText.get()+"and again,")

againButton = tk.Button(window, text="again", command=doItAgain)
againButton.pack()
messageText = tk.StringVar()
message = tk.Message(window, textvariable=messageText, width=300)
messageText.set("do it again,")
message.pack()


sepframe2 = tk.Frame(window, width=120, height=3, bg="black",)
sepframe2.pack()


##frame
frame_1 = tk.Frame(window, width=200, height=100, bg='white')
frame_2 = tk.Frame(window, width=200, height=100, bg='yellow')

frameButton_1_1 = tk.Button(frame_1, text="Button #1 inside Frame #1")
frameButton_1_2 = tk.Button(frame_1, text="Button #2 inside Frame #1")
frameButton_2_1 = tk.Button(frame_2, text="Button #1 inside Frame #2")
frameButton_2_2 = tk.Button(frame_2, text="Button #2 inside Frame #2")

frameButton_1_1.place(x=10, y=10)
frameButton_1_2.place(x=10, y=50)
frameButton_2_1.grid(column=0, row=0)
frameButton_2_2.grid(column=1, row=1)

frame_2.pack()
frame_1.pack()


sepframe3 = tk.Frame(window, width=120, height=3, bg="black",)
sepframe3.pack()


##label farme
lfrm1 = tk.LabelFrame(window, text="label frame 1", width=200, height=100, bd="8")
lfrm2 = tk.LabelFrame(window, text="label frame 2", width=200, height=100, bg="light blue", labelanchor="sw")

lframeButton_1_1 = tk.Button(lfrm1, text="button #1 inside Lframe #1")
lframeButton_1_2 = tk.Button(lfrm1, text="button #2 inside Lframe #1")
lframeButton_2_1 = tk.Button(lfrm2, text="button #1 inside Lframe #2")
lframeButton_2_2 = tk.Button(lfrm2, text="button #2 inside Lframe #2")

lframeButton_1_1.place(x=10, y=10)
lframeButton_1_2.place(x=10, y=50)
lframeButton_2_1.grid(column=0, row=0)
lframeButton_2_2.grid(column=1, row=1)

lfrm1.pack()
lfrm2.pack()

window.mainloop()