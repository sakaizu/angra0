from tkinter.constants import W
import pyautogui as ag
import time

currentpos = ag.position()

print(currentpos)
ag.moveRel(500, 0, 2)



print("end")