from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Firefox()

# Go to your page url
driver.get('https://ais.usvisa-info.com/en-ir?visa_type=niv')

button_element = driver.find_element_by_name('commit')
button_element.click()
time.sleep(5)
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.close()

for tag in soup.find_all("li"):
    if "Student Visas:" in tag.text:
        print("{0}: {1}".format(tag.name, tag.text))

# print(test)
exit()


ankara_after = soup.find("span", {"id": "lblAnkaraStu"}).text
yerevan_after = soup.find("span", {"id": "lblYerevanStu"}).text
dubai_after = soup.find("span", {"id": "lblYerevanStu"}).text
dataFile = open("data.html", "w+")
dataFile.seek(0)
dataFile.write(driver.page_source)
dataFile.close()



