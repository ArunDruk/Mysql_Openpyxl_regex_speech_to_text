from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
url = "https://opensource-demo.orangehrmlive.com/"

driver.implicitly_wait(10)
driver.get(url)
time.sleep(3)
print(driver.title)
driver.find_element_by_id("txtUsername").send_keys("arun")
time.sleep(3)
driver.find_element_by_id("txtPassword").send_keys("admin123")
time.sleep(3)
ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
time.sleep(3)
error_msg=driver.find_element_by_xpath("//input[@id='btnLogin']/following-sibling::span")

print(error_msg.text)