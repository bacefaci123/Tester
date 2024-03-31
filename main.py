from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import *
import colorama
from colorama import Fore, Back, Style
from colorama import init
import time
init()


driver = webdriver.Chrome()


class Scraper:
    def __init__(self , page):
        self.page = page
    def OpenPageAndScroll(self,ScrollingTime):
        self.ScrollingTime = ScrollingTime
        driver.get(self.page)
        element = driver.find_element(By.CLASS_NAME, "leaderboard--container")
        element.click()
        html = driver.find_element(By.TAG_NAME, 'html')
        print(f"Scroling for {self.ScrollingTime} seconds...")
        for i in range(self.ScrollingTime):
            html.send_keys(Keys.END)
            time.sleep(1)
    def ScrapeListAndWriteFile(self):
        names = driver.find_element(By.XPATH,"/html/body/div/main/section[2]/div/div[3]/div/div[1]/div[2]/div/div/div/div").text
        toList = names.split()
        new_list = [number for number in toList if not number.isdigit()]
        print(Fore.GREEN , "[STATUS]" + Fore.WHITE , "Writing account dump ...")
        file = open("dump.txt" , "w" , encoding="utf8")
        for i in range(len(new_list)):
            print(new_list[i])
            file.write(new_list[i]+"\n")
        file.close()
        print(Fore.GREEN ,"[STATUS]" , Fore.WHITE , "Dump written!")




f = open("sp.txt" , "r")
f = f.read()
f = str(f)


p = Scraper(f"https://superprono.superbet.ro/ro/leaderboard/overall/{f}")
p.OpenPageAndScroll(130)
p.ScrapeListAndWriteFile()
