 ### When the webpage is asking for Authentication as soon as open the webpage in the form of pop-up
 ## You have to enter the credentials in the URL itself .

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(3)
# driver.quit()