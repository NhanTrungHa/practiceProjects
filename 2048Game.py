#! python3
# 2048Game.py - Opens up website and randomly sends keystrokes to play game.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Edge()
browser.get('https://play2048.co/')
htmlElem = browser.find_element_by_tag_name('html')
for presses in range(1000):
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.LEFT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.RIGHT)
