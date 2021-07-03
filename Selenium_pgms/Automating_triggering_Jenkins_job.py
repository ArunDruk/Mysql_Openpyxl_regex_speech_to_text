
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

url = "https://testwin.epfin.coxautoinc.com/"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get(url)

driver.find_element_by_xpath("//div[@class ='login']/a/b").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@id ='j_username']").send_keys("akumar3")
time.sleep(2)
driver.find_element_by_xpath("//input[@name='j_password']").send_keys("Welcome@2020")
time.sleep(2)
driver.find_element_by_xpath("//input[@name='Submit']").click()
time.sleep(2)

