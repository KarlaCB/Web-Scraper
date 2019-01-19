import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

Driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
targetPage ="http://twilightsaga.wikia.com/wiki/Special_abilities"
Driver.get(targetPage)
title = Driver.find_element_by_class_name("page-header__title").text
print(title +"\n")
definition = Driver.find_element_by_xpath("//p[2]").text
print(definition + "\n")
heading = Driver.find_element_by_id("Active_talents").text
print(heading + "\n\n")

row_count = len(Driver.find_elements_by_xpath("//*[@id='mw-content-text']/table[1]/tbody/tr"))
col_count = len(Driver.find_elements_by_xpath("//*[@id='mw-content-text']/table[1]/tbody/tr[2]/td"))

# print(row_count)
# print(col_count)

first_part = "//*[@id='mw-content-text']/table[1]/tbody/tr["
second_part = "]/td["
third_part = "]"

for n in range(2, row_count+1):
    for m in range(1, col_count+1):
        final_path = first_part+str(n)+second_part+str(m)+third_part
        table_data = Driver.find_element_by_xpath(final_path).text
        print(table_data, end="" +"\n")
    print("")

print("\n\n")
heading1 = Driver.find_element_by_id("Passive_talents").text
print(heading1 + "\n\n")

row_count = len(Driver.find_elements_by_xpath("//*[@id='mw-content-text']/table[2]/tbody/tr"))
col_count = len(Driver.find_elements_by_xpath("//*[@id='mw-content-text']/table[2]/tbody/tr[2]/td"))

first_part = "//*[@id='mw-content-text']/table[2]/tbody/tr["
second_part = "]/td["
third_part = "]"

for n in range(2, row_count+1):
    for m in range(1, col_count+1):
        final_path = first_part+str(n)+second_part+str(m)+third_part
        table_data = Driver.find_element_by_xpath(final_path).text
        print(table_data, end="" +"\n")
    print("")

Driver.quit()