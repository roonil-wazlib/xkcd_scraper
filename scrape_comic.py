from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import shutil


def setup_soup():
    """open link and get soup object"""
    #open xkcd in Firefox
    driver = webdriver.Firefox()
    driver.get("https://xkcd.com")
    
    #get content as soup
    content = driver.page_source
    return driver, BeautifulSoup(content, "lxml")


def get_title(soup):
    """retrieve comic title"""
    title_div = soup.find(id="ctitle")
    return title_div.text
    
    
def get_comic(soup):
    """retrieve image src and mouse-over text"""
    comic_div = soup.find(id="comic")
    comic = comic_div.img
    mouseover_text = comic_div.img['title']
    return comic, mouseover_text
    
    
def get_middle_text(soup):
    """
    Get a pile of text out of the middle container that
    somewhere in it has the comic number
    """
    num_div = soup.find(id="middleContainer")
    return num_div.text


def get_comic_number(text):
    """extract comic number from big blob of text"""
    line_list = text.split("\n")
    for line in line_list:
        if line.split(" ")[0] == "Permanent":
            return line[-5:-1]
    else:
        return "???"
    
    
def download_image(comic, driver):
    """retrieve image src and download from there to local directory"""
    
    #rewrite image source and download image
    src = "http://" + comic['src'][2:]
    driver.get(src)
    driver.quit() #close browser
    
    resp = requests.get(src, stream=True)
    #write file to local folder
    local_file = open('/home/user1/Desktop/xkcd_scrape/latest_comic.png', 'wb')
    #Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)
    
    del resp
    
    
def set_comic_info(title, number, mouseover):
    """Set the display text in xkcd_info.txt"""
    file = open('/home/user1/Desktop/xkcd_scrape/xkcd_info.txt', 'w')
    file.write("\n\nxkcd {}: {} \n\n{}\n\n\n".format(number, title, mouseover))
    file.close()    
    
    
def main():
    #retrieve all the info
    driver, soup = setup_soup()
    title = get_title(soup)
    comic, mouseover = get_comic(soup)
    middle_txt = get_middle_text(soup)
    comic_number = get_comic_number(middle_txt)
    
    #set up the data for set_desktop.sh and set_mouseover.sh
    download_image(comic, driver)
    set_comic_info(title, comic_number, mouseover)

main()
