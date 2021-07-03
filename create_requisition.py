from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(20)
wait=WebDriverWait(driver,200)
url = "https://core-stage.epfinnp.coxautoinc.com/OA_HTML/AppsLocalLogin.jsp"
driver.maximize_window()
driver.get(url)
username_input=wait.until(ec.presence_of_element_located((By.ID,"usernameField")))
username_input.send_keys("emackay1")
time.sleep(1)
driver.find_element_by_id("passwordField").send_keys("oracle123")
time.sleep(1)
ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
iproc_user_element=wait.until(ec.presence_of_element_located((By.XPATH,"//div[contains(text(), 'CAI US iPROC USER')]//preceding::img[2]")))
assert driver.title == 'Home'
iproc_user_element.click()
time.sleep(2)
driver.find_element_by_xpath("//div[contains(text(), 'iProcurement Home Page')]").click()
assert driver.title == "Oracle iProcurement: Shop"
time.sleep(2)
wait.until(ec.presence_of_element_located((By.ID,"ICXPOR_NONCATALOG"))).click()
time.sleep(2)
item_type_element=wait.until(ec.presence_of_element_located((By.XPATH,"//select[@id='ItemType']")))
drop_down_box=Select(item_type_element)
drop_down_box.select_by_visible_text("Services.I can provide description, rate and quantity")
time.sleep(3)
driver.find_element_by_xpath("//textarea[@id='ItemDescription']").send_keys("TST_REQ:29:08:02")
time.sleep(3)
# driver.find_element_by_xpath("//input[@id='Category']").send_keys("IT/ TELECOM.IT SERVICES.COMPUTER HARDWARE MAINTENANCE & SUPPORT.CAI")
driver.find_element_by_xpath("//input[@id='Category']").send_keys("IT")
ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
time.sleep(4)
# handles=driver.window_handles
# for handle in handles:
#     print(handle)
driver.switch_to_window(driver.window_handles[1])
time.sleep(2)
driver.find_element_by_xpath("//input[@id='N1:N8:4']").click()
time.sleep(2)
driver.find_element_by_xpath("//button[contains(text(),'Select')]").click()
time.sleep(1)
driver.switch_to_window(driver.window_handles[0])
time.sleep(4)

driver.find_element_by_xpath("//input[@id='Quantity']").send_keys("12")
driver.find_element_by_xpath("//input[@id='UnitOfMeasureTl']").send_keys("Each")
driver.find_element_by_xpath("//input[@id='RatePerUnit']").send_keys("220")
driver.find_element_by_xpath("//input[@id='SupplierOnNonCat']").send_keys("9015 PARTNERS LLC")
ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
time.sleep(4)
handles=driver.window_handles
for handle in handles:
    print(handle.title(),"\t", handle)
driver.switch_to.window(handles[1])
time.sleep(2)
driver.find_element_by_xpath("//input[@id='N1:N8:0']").click()
time.sleep(2)
driver.find_element_by_xpath("//button[contains(text(),'Select')]").click()
time.sleep(1)
driver.switch_to.window(handles[0])
time.sleep(4)
# driver.find_element_by_xpath("//input[@id='SupplierSiteOnNonCat']").send_keys("ATGSANAN01")
driver.find_element_by_id("AddToCart").click()



