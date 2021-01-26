import os
import shutil
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


url = "https://www.chrisburkard.com/Stills/Adventure"

web_r = requests.get(url)
web_soup = BeautifulSoup(web_r.text, 'html.parser')

print(web_soup.findAll("img"))

#<img src=''/>


driver = webdriver.Firefox()
driver.get(url)

time.sleep(5)
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')
print(len(sel_soup.findAll("img")))
images = []
for i in sel_soup.findAll("img"):
    src = i["src"]
    images.append(src)
print(images)
current_path = os.getcwd()
for img in images:
    try:
        file_name = os.path.basename(img)
        img_r = requests.get(img, stream=True)
        new_path = os.path.join(current_path, "images", file_name)
        with open(new_path, "wb") as output_file:
            shutil.copyfileobj(img_r.raw, output_file)
        del img_r
    except:
        pass

