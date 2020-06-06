from selenium import webdriver
import time

driver=webdriver.Chrome()
url="http://www.msn.com"
driver.get(url)
driver.maximize_window()
time.sleep(2)
webpage_title="MSN India | Breaking News, Entertainment, Latest Videos, Outlook"

assert driver.title == webpage_title
time.sleep(2)
driver.find_element_by_link_text("LIFESTYLE").click()
time.sleep(10)

driver.close()
