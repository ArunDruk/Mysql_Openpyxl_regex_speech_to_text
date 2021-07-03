
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome(ChromeDriverManager().install())
url="http://tinyupload.com/"
driver.implicitly_wait(10)

driver.get(url)
time.sleep(5)

path="C:\\Users\\akumar6\\Documents\\Journal_import_165427513.txt"
driver.find_element_by_xpath("//input[@name='uploaded_file']").send_keys(path)

time.sleep(5)






