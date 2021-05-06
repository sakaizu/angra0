from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import platform
import time
import pyperclip
import pyautogui as pg

if platform.system() == "Darwin":
    print("sys = Mac")
else:
    print("sys = Win")

op = webdriver.ChromeOptions().add_argument("--incognito")
driver  = webdriver.Chrome("D:\OneDrive\ChromeDriver\chromedriver.exe", options = op)

driver.get("https://nid.naver.com/nidlogin.login")

time.sleep(0.15)

id = "angra0"
pw = "sakai3512!"

# driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
# driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")

tag_id = driver.find_element_by_name('id')
tag_pw = driver.find_element_by_name('pw')
tag_id.clear()

time.sleep(0.5)
tag_id.click()
pyperclip.copy(id)
# tag_id.send_keys(Keys.CONTROL, 'v')
pg.hotkey('ctrl', 'v')

time.sleep(1)

tag_pw.click()
pyperclip.copy(pw)
# tag_pw.send_keys(Keys.CONTROL, 'v')
pg.hotkey('ctrl', 'v')

time.sleep(1)

driver.find_element_by_xpath('//*[@id="log.login"]').click()