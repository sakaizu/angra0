import platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
import time
import os
from PIL import Image

from urllib.request import Request, urlopen, urlretrieve

def delAllFiles():
    files = os.listdir(downloadPath)
    for i in files:
        print(i)
        filesize = os.path.getsize(downloadPath + str(i))
        print("size = %s" %filesize)


userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'



searchTEXT = "space 4k wallpaper"
MaxCount = 30


if platform.system() == "Darwin":
    print("platform = mac")
    downloadPath = "python/study/Web/DL/" 
    driver = webdriver.Chrome('/Users/seojanghyeob/OneDrive/ScriptWorks/Workspace/python/study/Web/driver/chromedriverm1')
else:
    print("platform = pc")
    downloadPath = "D:\OneDrive\ScriptWorks\Workspace\python\study\Web\DL/"
    driver  = webdriver.Chrome("D:\OneDrive\ChromeDriver\chromedriver.exe")



driver.get('https://www.google.co.kr/imghp?hl=ko&ogbl')

searchBar = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
searchBar.send_keys(searchTEXT)
searchBar.send_keys(Keys.RETURN)

time.sleep(1)
driver.execute_script("window.scrollTo(0, 3000)")
time.sleep(0.25)
driver.execute_script("window.scrollTo(0, 5000)")
time.sleep(1)


# imgs = driver.find_elements_by_class_name("rg_i.Q4LuWd")
imgs = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
print("\nFind Targets = %s \n\n" %len(imgs))


imgNum = 0
for i in imgs:
    i.click()

    time.sleep(1)
    target = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img')
    src = target.get_attribute("src")

    trycount = 0
    while src[0] != "h":
        if trycount < 10:
            print("target is not load yet = Waiting")
            time.sleep(1)
            arget = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img')
            src = target.get_attribute("src")
            trycount += 1
        else:
            src = None
            print("Loadtime expired -- Try Next Target -- \n")
            break

    print("count = " + str(imgNum))
    print(target.get_attribute("alt"))
    print(src)

    imgurl = src

    if imgurl != None:
        req = Request(imgurl,  headers={'User-Agent': userAgent})
        file = urlopen(req).read()

        with open(downloadPath + "img_" + str(imgNum) + ".jpg", 'wb') as f:
            f.write(file)

        im = Image.open(downloadPath + "img_" + str(imgNum) + ".jpg")
        w, h = im.size
        print("Resolution = " + str(w) + ", " + str(h))
        
        if h!= 2160:
            print("this is Not 4k - Delete Files \n")
            check = False
            os.remove(downloadPath + "img_" + str(imgNum) + ".jpg")
        else:
            print("found! -- Write Files -- \n")
            check = True

        # urlretrieve(str(imgurl), "python/study/Web/DL/img_" + str(imgNum) + ".jpg")
    else:
        check = False
    
    if check:
        imgNum+=1

    if imgNum > MaxCount:
        print("\n -- terminate --")
        delAllFiles()
        quit()






