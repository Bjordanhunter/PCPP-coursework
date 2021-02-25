import tkinter as tk

def rObserver(*args):
    print("reading")

def wObserver(id,ix,act):
    print("writing")

window = tk.Tk()

var = tk.StringVar() #BooleanVar, DoubleVar, IntVar
var.set("ABC")
rObsId = var.trace("r", rObserver)
wObsId = var.trace("w", wObserver)

var.set(var.get()+"d")
var.trace_vdelete("r",rObsId)
var.set(var.get()+"e")
var.trace_vdelete("w",wObsId)
var.set(var.get()+"f")
print(var.get())
