import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

Driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
targetPage ="http://coreyms.com"
Driver.get(targetPage)
headline = Driver.find_element_by_class_name("entry-title").text
print(headline + "\n")
article = Driver.find_element_by_class_name("entry-content").text
print(article)
time.sleep(10)
Driver.quit()

