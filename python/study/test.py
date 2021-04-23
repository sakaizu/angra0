from tkinter import *
root = Tk()
root.title("MainWindows")
root.geometry("640x480")

def run1():
    print(txt.get("1.0", END))
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)

btn1 = Button(root, text= "push")
btn1.pack()

btn3 = Button(root, fg = "red", bg = "yellow", text= 'Print', command=run1)
btn3.pack()


txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "insert num")

e = Entry(root, width=30)
e.pack()


root.mainloop()

