
import pytest
from selenium.webdriver import Chrome
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("init_driver")
class BaseTest():
    pass

class Test_Hubspot(BaseTest):
    @pytest.mark.parametrize("username, password",[("admin@gmail.com","admin123"),("arundruk@gmail.com","arun123")])
    def test_login1(self,username,password):
        """
        This method is used to login to hub spot application
        :param username:
        :param password:
        :return:
        """
        # driver= Chrome(ChromeDriverManager().install())
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID,'username').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.ID,'password').send_keys(password)


