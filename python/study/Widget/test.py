from tkinter import *
from tkinter import ttk
import os
import random
import platform
import time
import sys

if platform.system() == "Darwin":
    print("Current System is MacOS")

currentPath = os.path.dirname(os.path.realpath(__file__))

root = Tk()
root.title("MainWindows")
root.geometry("640x480")

# ----------------Menu Def-------------------

def clkOpenFile():
    print("test")

def clkExit():
    sys.exit()
# ----------------File Menu-------------------

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open File", command=clkOpenFile, state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=clkExit)

menu.add_cascade(label="File", menu= menu_file)

# ----------------Edit Menu-------------------

menu_edit = Menu(menu, tearoff=0)
menu_edit.add_command(label="Open File", command=clkOpenFile)

menu.add_cascade(label="Edit", menu= menu_edit)




root.configure(bg="#E9E9E9")
root.config(menu=menu)

def curlist():
    for i in listbox.curselection():
        print(listbox.get(i))
        txtBox.insert(END, "%s \n" %listbox.get(i))

def runDebug():

    linetext = txtLine.get()

    txtBox.delete("1.0", END)
    txtLine.delete(0, END)

    txtBox.insert(END, "combobox = %s \n" %cmbBox.get())
    txtBox.insert(END, "radio = %s \n" %radiovar.get())
    txtBox.insert(END, "input = %s \n" %linetext)
 
    curlist()

    txtBox.insert(END, "True" if chkVar.get()==1 else "False") #if문 한줄코드

    for i in range(101):
        time.sleep(0.005)
        p_var.set(i)
        pbar.update()


btn_print = ttk.Button(root, text= 'Excute', command=runDebug)
btn_print.pack()

values = [i for i in range(1, 11)]
cmbBox = ttk.Combobox(root, height = 5, values=values, state="readonly")
# cmbBox.set("select proxy")
cmbBox.current(0)
cmbBox.pack()


radiovar = IntVar()
raBtn1 = ttk.Radiobutton(root, text="test", value=1, variable=radiovar)
raBtn2 = ttk.Radiobutton(root, text="my", value=2, variable=radiovar)
raBtn3 = ttk.Radiobutton(root, text="check", value=3, variable=radiovar)

raBtn1.pack()
raBtn2.pack()
raBtn3.pack()


chkVar = IntVar()
chkbox = ttk.Checkbutton(root, text="use for this", variable=chkVar)
chkbox.pack()


txtLine = ttk.Entry(root, width=30)
txtLine.pack()
txtLine.insert(0, "Insert Text")


listbox = Listbox(root, selectmode="extended",width=30, height=5)
for i in range(3):
    listbox.insert(i, "%s Count" %random.randrange(0, 100))

listbox.pack()



# ----------debug box-----------

txtBox = Text(root, width=30, height=10)
txtBox.pack()
txtBox.insert(END, "print space")

p_var = DoubleVar()
pbar = ttk.Progressbar(root, length=200, maximum=100, mode="determinate", variable=p_var)
pbar.pack()



root.mainloop()
