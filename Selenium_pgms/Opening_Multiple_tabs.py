from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(3)
# driver.maximize_window()

url1="http://www.google.com"
url4="http://www.msn.com"
url2="http://www.yahoo.com"
url3="http://www.rediff.com"

driver.get(url1)
time.sleep(5)

driver.find_element_by_xpath("//input[@type='text']").send_keys("msn india")
ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()  # To Press "ENTER" in Keyboard
time.sleep(3)

element=driver.find_element_by_link_text("India")

for i in range(3):
    ActionChains(driver).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
    time.sleep(5)

Handles=driver.window_handles

# for Handle in Handles:
#     print(Handle)

driver.switch_to.window(Handles[1]) # this comes towards the right side tab, higher the number of window handles it comes towards left.
driver.get(url2)
time.sleep(5)
print(driver.title)

driver.switch_to.window(Handles[2])
driver.get(url3)
time.sleep(5)
print(driver.title)

driver.switch_to.window(Handles[3])
driver.get(url4)
time.sleep(5)
print(driver.title)
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(4)
# #
# driver.execute_script("window.open('http://www.rediff.com','new_window');")
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(4)


time.sleep(4)
# driver.quit()






