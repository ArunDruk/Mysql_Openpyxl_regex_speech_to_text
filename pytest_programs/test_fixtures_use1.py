
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("___________________________Setup________________________")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

    yield
    print("___________________________Tear Down________________________")
    driver.quit()

def test_google_title(init_driver):  ### Here we passing the fixture name in the method.
    assert driver.title == "Google11"

@pytest.mark.usefixtures("init_driver")   ### We can use markers to use the fixtures as an alternative instead of passing fixture name in the method like previous method
def test_google_url():
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"