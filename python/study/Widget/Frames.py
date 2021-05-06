from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Frames Testing")
root.geometry("640x480")

leftframe = LabelFrame(root, text="left frame", relief="groove", bd=2, width=200, height=100, padx=10, pady=10)
rightframe = LabelFrame(root, text="right frame", relief="groove", bd=2)

leftframe.pack(side="top", fill="both")
rightframe.pack(side="right", fill="both", expand="True")

inleftframe = LabelFrame(leftframe, text="f1", relief="ridge", bd=2, padx=60, pady=10)
inrightframe = LabelFrame(leftframe, text="f2", relief="ridge", bd=2, padx=60, pady=10)

inleftframe.pack(side="left", fill="both")
inrightframe.pack(side="right", fill="both")

ttk.Label(inleftframe, text="testlabel").pack()
ttk.Label(inrightframe, text="testlabel").pack()

# ttk.Button(leftframe, text= "sidepass").pack()
# ttk.Button(leftframe, text= "sidepass").pack()
ttk.Button(rightframe, text= "sidepass").pack()
ttk.Button(rightframe, text= "sidepass").pack()

root.mainloop()
