from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import os
from pystyle import *
import time
import random
import string
import requests

os.system('title 0xTwitterFucker ^| By KynZay#4521 ^| using : Twitter Creator')

print(Colors.green + "         [" + Colors.gray + "+" + Colors.green + "]" + Colors.gray + " starting up..")
datem = "5"
datej = "21"
datea = "2000"
driver: WebDriver = webdriver.Chrome(ChromeDriverManager().install())
email = ("").join(random.choices(string.ascii_letters + string.digits, k = 8)) + "@gmail.com"
password = ("0xBotterEveryware")
usr = ("").join(random.choices(string.ascii_letters + string.digits, k = 8))
print(Colors.green + "         [" + Colors.gray + "+" + Colors.green + "]" + Colors.gray + " loaded !")

driver.get("https://twitter.com/i/flow/signup")
time.sleep(5)
driver.find_element_by_xpath("""//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]""").click()
time.sleep(0.5)
# driver.find_element_by_xpath("""//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/span""").click()
# time.sleep(0.5)
driver.find_element_by_xpath("""//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/label/div/div[1]""").clear()
time.sleep(0.5)
driver.find_element_by_xpath("""//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/label/div/div[1]""").send_keys(usr)
time.sleep(0.5)
driver.find_element_by_xpath("""//*[@id="SELECTOR_10"]""").clear()
time.sleep(0.5)
driver.find_element_by_xpath("""//*[@id="SELECTOR_10"]""").send_keys(datem)
time.sleep(0.5)
driver.find_element_by_xpath("""//*[@id="SELECTOR_11"]""").clear()
time.sleep(0.5)
driver.find_element_by_xpath("""//*[@id="SELECTOR_11"]""").send_keys(datej)
time.sleep(0.5)
driver.find_element_by_xpath("""//*[@id="SELECTOR_12"]""").clear()
time.sleep(0.5)
driver.find_element_by_xpath("""//*[@id="SELECTOR_12"]""").send_keys(datea)

with open("Created.txt", "a") as f:
    f.write(f'{email}:{password}:{usr}\n')