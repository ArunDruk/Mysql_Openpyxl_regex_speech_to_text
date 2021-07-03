from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.speedtest.net/"

driver.get(url)
time.sleep(10)

element=driver.find_element_by_partial_link_text("View Map")
driver.execute_script("arguments[0].scrollIntoView();",element)

# ########################################################### Method 1 (scroll till page end) ###########################################################
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
# time.sleep(10)

############################################################## Method 2 (scroll till page end) ########################################################
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# time.sleep(10)

############################################################## Method 3 (using Action chain Keys) ##############################################################
# ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.END).key_up(Keys.CONTROL).perform()
# time.sleep(10)