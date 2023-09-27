# Write your code here :-)
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')

elem = browser.find_element(By.CLASS_NAME,'bookcover')
print('Found <%s> element with that class name!' % (elem.tag_name))

