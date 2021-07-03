from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
# url="http://www.goodreturns.in"
url="https://developer.salesforce.com/"

driver.get(url)
wait=WebDriverWait(driver,10)

elements=wait.until(ec.presence_of_all_elements_located((By.XPATH,"//h3[contains(text(),'Developer Centers')]/following-sibling::ul")))
# wait.until(ec.text_to_be_present_in_element((By.ID,"IDName"),'INDIA'))f

for ele in elements:
    print(ele.text)

driver.quit()




