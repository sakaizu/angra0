import pyautogui as pg
import clipboard
import time

clipboard.copy("https://www.youtube.com/feed/history")

a = "https://www.youtube.com/feed/history"

pg.press('winleft')

pg.typewrite('chrome')
pg.press('enter')

time.sleep(0.3)

pg.press('hangul')

pg.hotkey('ctrl', 'v')
pg.press('enter')

