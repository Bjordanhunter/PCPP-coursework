import tkinter as tk
from tkinter import messagebox as mbox

def question_yes_no():
    answer = mbox.askyesno("question","yes or no")
    print(answer)

def question_ok_cancel():
    answer = mbox.askokcancel("?", "ok or cancel")
    print(answer)

def question_retry_cancel():
    answer = mbox.askretrycancel("?", "retry or cancel")
    print(answer)

def question_question():
    answer = mbox.askquestion("?", "yes/no question")
    print(answer)

def error():
    answer = mbox.showerror("!", "error message")
    print(answer)

def warn():
    answer = mbox.showwarning("!", "warning message")
    print(answer)

def yes_no_cancel():
    answer = mbox.askyesnocancel("?","yes, no, cancel")
    print(answer)

window = tk.Tk()
button_yes_no = tk.Button(window, text="ask question y/n", command=question_yes_no)
button_yes_no.pack()

button_ok_cancel = tk.Button(window, text="ask question ok/cancel", command=question_ok_cancel)
button_ok_cancel.pack()

button_retry_cancel = tk.Button(window, text="ask question retry/cancel", command=question_retry_cancel)
button_retry_cancel.pack()

button_question = tk.Button(window, text="ask question yes/no", command=question_question)
button_question.pack()

button_error = tk.Button(window, text="show error", command=error)
button_error.pack()

button_warn = tk.Button(window, text="show warning", command=warn)
button_warn.pack()

button_yes_no_cancel = tk.Button(window, text="ask question yes/no/cancel", command=yes_no_cancel)
button_yes_no_cancel.pack()

window.mainloop()
