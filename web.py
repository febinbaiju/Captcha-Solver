from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from KNN import get_captcha
import cv2

mobile_no = input("Input Mobile Number: ")
message = input("Input the message to be sent: ")

options = Options()
options.headless = True

profile = webdriver.FirefoxProfile()
profile.set_preference("webdriver.load.strategy", "unstable")
profile.update_preferences()
obj = webdriver.Firefox(firefox_profile=profile,timeout=5,options=options)
obj.get("http://www.afreesms.com/intl/india")
obj.execute_script("return window.stop")


cookie_accept = obj.find_element_by_xpath("//a[@class='cc-btn cc-dismiss']")
cookie_accept.click()
verification = obj.find_element_by_xpath("//input[@class='auto']")
captcha = obj.find_element_by_id("captcha")
obj.execute_script("arguments[0].style = 'border:1px solid #000000;';",captcha)
verification.location_once_scrolled_into_view
obj.save_screenshot("image.png")

#get captcha from screenshot
captcha = cv2.imread("image.png")
captcha = captcha[0:28,506:582]
cv2.imwrite("image.png",captcha)
captcha_found = get_captcha("image.png")
if len(captcha_found)<1:
    print("CAPTCHA FAILED TO IDENTIFY")
    exit

elem = obj.find_element_by_xpath("//input[2]")
elem.send_keys(mobile_no)
textarea = obj.find_element_by_xpath("//textarea[1]")
textarea.send_keys(message)
verification.send_keys(captcha_found)
verification.send_keys(Keys.RETURN)


obj.close()