from selenium import webdriver
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# driver=webdriver.Chrome()
# driver= webdriver.Ie(IEDriverManager().install())
driver=webdriver.Edge(EdgeChromiumDriverManager().install())

url="http://google.com"
driver.get(url)

time.sleep(5)
# driver.maximize_window()
driver.close()