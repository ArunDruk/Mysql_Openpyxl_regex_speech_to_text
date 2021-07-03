from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

url = "https://csa.workbench.manheim.man-silo5.com"



@pytest.fixture(scope='class')  # scope='module'
def test_setup_method(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    wait = WebDriverWait(driver, 100)
    request.cls.driver=driver
    yield
    driver.quit()

@pytest.mark.usefixtures("test_setup_method")
class Test_Login():
    # @pytest.fixture(scope='module')
    # def test_setup_method(self):
    #     global driver
    #     driver = webdriver.Chrome()
    #     wait = WebDriverWait(driver, 100)
    #     yield
    #     driver.quit()

    def test_login_method(self): #,test_setup_method):
        self.driver.get(url)
        userid_obj=self.wait.until(ec.presence_of_element_located((By.XPATH,"//input[@id='userid']")))
        userid_obj.send_keys("CSA-Issue-3")
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys("Pswd11-CSA")
        time.sleep(2)
        ActionChains(self.driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
        time.sleep(2)
        ActionChains(self.driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        self.wait.until(ec.title_contains(("Search Customer")))
        assert self.driver.title == "Search Customer"
        time.sleep(5)

    # def test_logout(self,test_setup_method):
    #     self.driver.find_element_by_xpath("//a[@id='ewb-logout']").click()
    #     time.sleep(5)

# AttributeError: 'Test_Login' object has no attribute 'driver'
