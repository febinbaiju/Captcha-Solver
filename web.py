from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import requests

mobile_no = input("Input Mobile Number: ")
message = input("Input the message to be sent: ")

options = Options()
options.headless = True
obj = webdriver.Firefox()
obj.get("http://www.afreesms.com/intl/india")
verification = obj.find_element_by_xpath("//input[@class='auto']")
verification.location_once_scrolled_into_view
obj.save_screenshot("image.png")
elem = obj.find_element_by_xpath("//input[2]")
elem.send_keys(mobile_no)
textarea = obj.find_element_by_xpath("//textarea[1]")
textarea.send_keys(message)
verification.send_keys("124")
verification.send_keys(Keys.RETURN)