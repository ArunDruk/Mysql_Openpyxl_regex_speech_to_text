from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("http://ww25.testingworld.com/")
time.sleep(6)
driver.find_element_by_xpath("//a[contains(text(),'Automation Testing']").click()
#driver.find_element_by_link_text("Automation Testing").click()
#driver.find_element_by_xpath("//*[@id='adBlock']/table/tbody/tr[4]/td/div/div/div/div/a").click()
driver.close()



