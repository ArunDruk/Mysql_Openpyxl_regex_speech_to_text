from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
url="http://www.seleniumhq.org"

driver.get(url)
driver.maximize_window()
time.sleep(4)
# driver.find_element_by_xpath("//input[@title='search']").send_keys("Chrome driver")
# time.sleep(4)
# driver.find_element_by_class_name("search-icon").click()
# time.sleep(4)
####################################################################################################
download_element=driver.find_element_by_link_text("Downloads")
print(download_element.text)
print(download_element.get_attribute('href'))
download_element.click()
download_element.send_keys(Keys.ENTER)

####################################################################################################
time.sleep(4)
driver.close()