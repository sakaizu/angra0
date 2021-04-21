import pyautogui as ag
import time

currentpos = ag.position()

print(currentpos)

ag.moveTo(1000, 1200)
ag.typewrite(["winleft"])

time.sleep(0)

ag.typewrite("foobar")
ag.typewrite(["enter"])

time.sleep(0.25)

#ag.hotkey('alt', 'f4')

ag.typewrite(['alt', 'l', 's'])

ag.typewrite("evangelion")

time.sleep(0.3)

ag.typewrite(["enter"])

ag.hotkey('alt', 'f4')


print("end")