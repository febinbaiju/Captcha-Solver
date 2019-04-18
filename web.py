from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
obj = webdriver.Firefox()
obj.get("http://www.afreesms.com/intl/india")
elem = obj.find_element_by_xpath("//input[2]")
elem.send_keys("9539639217")
textarea = obj.find_element_by_xpath("//textarea[1]")
textarea.send_keys("hello world")
print("hello world")