from tkinter import *
from tkinter import ttk
import pyautogui as pg
import time

root = Tk()
root.title("Search & Run")
root.geometry("500x150")
root.configure(bg="#E9E9E9")

def run():
    if inputLine.get() != "":
        print(inputLine.get())
        for i in range(101):
            prbarVar.set(i)
            perlabel.config(text = i)
            time.sleep(0.01)
            prbar.update()

        pg.hotkey("command", "space")
        pg.typewrite(inputLine.get())
        time.sleep(0.1)
        pg.press("enter")
        inputLine.delete(0, END)
    else:
        inputLine.insert(0, "type anything")
        print("nothing")

label1 = ttk.Label(root, text="please input strings")
label1.pack()

inputLine = ttk.Entry(root, width="35")
inputLine.pack()


runBtn = ttk.Button(root, text="Run", command=run)
runBtn.pack()

prbarVar = DoubleVar()
prbar = ttk.Progressbar(root, maximum=100, variable=prbarVar)
prbar.pack()


perlabel = ttk.Label(root, text="")
perlabel.pack()

root.mainloop()
