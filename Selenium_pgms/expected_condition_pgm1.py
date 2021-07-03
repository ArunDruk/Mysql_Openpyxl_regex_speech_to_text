################################ Different types of ExpectedConditions for Explicit wait:##############################################################
# title_is  -> Checks for the complete title
# title_contains -> Checks whether the title contains any word which we are giving
# url_contains ->
# url_to_be
# presence_of_element_located -> The Element is available on the page to do operations
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located -> Suppose we have multiple elements to be located, then we use this condition, which checks for all elements
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected -> This condition is used mainly for Dropdown box and check box
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present
############################################################################################################################
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
############################################################
# from webdriver_manager.chrome import ChromeDriverManager
# pip install webdriver_manager
# driver=webdriver.Chrome(ChromeDriverManager().install()) # This will install the Chrome webdriver
############################################################
driver=webdriver.Chrome()
driver.get('http://app.hubspot.com/login')
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)
########################################### Validating whether opened the right webpage ############################################
# Login_page=wait.until(ec.title_contains("HubSpot")) # This is going to return bool value 'True' or 'False'
#
# if(Login_page == True):
#     print("Successfully Launched : " + str(driver.title))
# else:
#     print("Not able to open HubSpot Login Window")
######################################################################################################################
email_address=wait.until(ec.presence_of_element_located((By.ID,'username'))) # To validate whether this element is located in webpage
# presence_of_element_located, we need to pass single element, so enclosing in double braces
email_address.send_keys("arundruk@ymail.com")
# print(driver.title)

# wait=WebDriverWait(driver,10)
# wait.until(ec.title_contains("Hubspot"))
#
# alert=wait.until(ec.alert_is_present())
# print(alert.text)
# alert.accept()
#
# sign_up_link=wait.until(ec.element_to_be_clickable(By.LINK_TEXT,'Sign up'))
#
# footer_links=wait.until(ec.presence_of_all_elements_located(By.CSS_SELECTOR,'ul.footer'))