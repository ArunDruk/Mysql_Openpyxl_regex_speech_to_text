
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pytest import fixture
import time


url = "https://csa.workbench.manheim.man-silo5.com"
# @fixture(scope="session")
# def chrome_browser():
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.maximize_window()
#     yield driver
#     driver.close()


def test_login(chrome_browser):
    driver=chrome_browser
    driver.get(url)
    driver.find_element_by_id("userid").send_keys("CSA-Issue-3")
    time.sleep(2)
    driver.find_element_by_id("password").send_keys("Pswd11-CSA")
    time.sleep(2)
    driver.find_element_by_xpath("//input[@value='Log In']").click()
    time.sleep(5)
    print("Login Successful")

def test_title(chrome_browser):
    driver=chrome_browser
    print(driver.title)
    assert driver.title == "Search Customer"

