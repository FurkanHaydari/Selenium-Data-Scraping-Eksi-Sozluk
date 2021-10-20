from selenium import webdriver
import random
import time

browser = webdriver.Firefox()

url = "https://eksisozluk.com/ogrenildiginde-ufku-iki-katina-cikaran-seyler--2593151?p="

pageCount = 1
entries = []
entryCount = 1

while pageCount <= 353:
    newUrl = url + str(pageCount)
    browser.get(newUrl)
    
    elements = browser.find_elements_by_css_selector(".content")

    for element in elements:
        entries.append(element.text)
    time.sleep(1)
    pageCount +=1
    
pageCount=1

with open("entries.txt","w",encoding = "UTF-8") as file:
    for entry in entries:
        file.write(str(pageCount) + ".\n" + entry + "\n")
        file.write("********************************************\n")
        pageCount +=1

        


    
browser.close()


