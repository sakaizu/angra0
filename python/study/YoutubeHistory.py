import pyautogui as pg
import clipboard
import time

clipboard.copy("https://www.youtube.com/feed/history")

pg.hotkey('command', 'space')

pg.typewrite('chrome')
pg.press('enter')

time.sleep(0.3)

pg.hotkey('command', 't')


time.sleep(0.3)

pg.hotkey('command', 'v')
pg.press('enter')

