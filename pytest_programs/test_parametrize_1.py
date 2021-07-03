import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# @pytest.mark.parametrize("num, res",[(1,11),(2,22),(3,30),(4,44)])
# def test_calc1(num,res):
#     assert 11*num == res

url = "https://opensource-demo.orangehrmlive.com/"

@pytest.fixture(scope="session")
def login_method():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get(url)
    time.sleep(3)
    yield driver
    driver.quit()

#@pytest.mark.usefixtures("test_login_method")
def test_Login_orangeHRM(login_method):
    driver=login_method
    print(driver.title)
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    time.sleep(3)
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    time.sleep(3)
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(3)
    print("Login Successful")
    # error_msg = driver.find_element_by_xpath("//input[@id='btnLogin']/following-sibling::span")
    #
    # print(error_msg.text)

def test_verify_title(login_method):
    assert driver.title == "OrangeHRM"

