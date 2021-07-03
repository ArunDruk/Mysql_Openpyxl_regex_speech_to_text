from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(20)
wait=WebDriverWait(driver,20)
url = "https://core-stage.epfinnp.coxautoinc.com/OA_HTML/AppsLocalLogin.jsp"

driver.get(url)
username_input=wait.until(ec.presence_of_element_located((By.ID,"usernameField")))
username_input.send_keys("emackay1")
time.sleep(2)
driver.find_element_by_id("passwordField").send_keys("oracle123")
time.sleep(1)
ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
iproc_user_element=wait.until(ec.presence_of_element_located((By.XPATH,"//div[contains(text(), 'CAI US iPROC USER')]//preceding::img[2]")))
assert driver.title == 'Home'
iproc_user_element.click()
reports_element=wait.until(ec.presence_of_element_located((By.XPATH,"//div[contains(text(), 'Reports')]/preceding::img[2]")))
reports_element.click()
run_element=wait.until(ec.presence_of_element_located((By.XPATH,"//div[contains(text(), 'Run')]")))
run_element.click()
time.sleep(2)



