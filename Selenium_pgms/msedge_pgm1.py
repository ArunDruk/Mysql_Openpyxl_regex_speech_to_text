### Run this Command to install the driver for Edge v >17
#### DISM.exe /Online /Add-Capability /CapabilityName:Microsoft.WebDriver~~~~0.0.1.0

from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

driver=webdriver.Edge(EdgeChromiumDriverManager().install())

url="http://google.com"
driver.get(url)

time.sleep(5)
# driver.maximize_window()
driver.close()