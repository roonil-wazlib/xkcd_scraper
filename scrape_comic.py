from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import shutil

driver = webdriver.Firefox()
driver.get("https://xkcd.com")

content = driver.page_source
soup = BeautifulSoup(content, "lxml")

div = soup.find(id="comic")
comic = div.img

src = "http://" + comic['src'][2:] #remove // from beginning of link
driver.get(src)
driver.quit()


resp = requests.get(src, stream=True)
# Open a local file with wb ( write binary ) permission.
local_file = open('/home/user1/Desktop/xkcd_scrape/latest_comic.png', 'wb')
# Set decode_content value to True, otherwise the downloaded image file's size will be zero.
resp.raw.decode_content = True
shutil.copyfileobj(resp.raw, local_file)
# Remove the image url response object.
del resp
