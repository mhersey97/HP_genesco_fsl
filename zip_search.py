from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

# launch browser
browser = webdriver.Chrome()
browser.get('https://www.zip-codes.com/distance_calculator.asp')
browser.implicitly_wait(10)

# open files
#source = browser.find_element_by_id('from')
#dest = browser.find_element_by_id('to')
#source.send_keys("03833")
#dest.send_keys("03824")
#press = browser.find_element_by_class_name('button.green')
#press.click()
#browser.implicitly_wait(10)

# read output
#distance = browser.find_element_by_class_name('mi').text
#print("distance is: ")
#print(distance)

# open files
f = open("fsl.txt", "r")
c = open("match.csv", "r")
match = open("match1.csv", "w")

for x in c:
    closest = "NULL"
    distance = 1000000
    cZip = re.split(r',', x)
    source = browser.find_element_by_id('from')
    press = browser.find_element_by_class_name('button.green')

    if cZip[1] != "#N/A" and int(cZip[1]) == 1 and cZip[2] == "NULL":
        source.send_keys(cZip[0][0:5])
        f.seek(0)
        for y in f:
            fZip = re.split(r'\t', y)
            dest = browser.find_element_by_id('to')
            dest.send_keys(fZip[1])
            press = browser.find_element_by_class_name('button.green')
            press.click()
            browser.implicitly_wait(15)

            d = browser.find_element_by_class_name('mi').text
            dist = float(d.replace(',',''))
            if dist < distance:
                distance = dist
                closest = fZip[0]

            browser.find_element_by_id('to').clear()
    
    if(distance < 1000000):
        print(cZip[0], " - ", closest)
    match.write(cZip[0])
    match.write(',')
    match.write(closest)
    match.write(',')
    match.write(str(distance))
    match.write(',\n')

    browser.find_element_by_id('from').clear()

f.close
c.close
match.close
