from selenium import webdriver
import time

driver =webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com")
time.sleep(2)
driver.execute_script("window.open('http://www.msn.com','new window')")
driver.switch_to.window(driver.window_handles[0])

driver.get("http://www.facebook.com")
time.sleep(2)
driver.execute_script("window.open('http://www.yahoo.com','new window')")
driver.switch_to.window(driver.window_handles[1])

