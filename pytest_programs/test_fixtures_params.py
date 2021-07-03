
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import pytest

@pytest.fixture(params=["chrome","firefor"],scope='class')
def init_driver(request):
    try:
        if request.param == "chrome":
            web_driver=webdriver.Chrome(ChromeDriverManager().install())
        if request.param == "firefox":
            web_driver =webdriver.Firefox(executable_path=GeckoDriverManager().install())
        request.cls.driver = web_driver
        yield
        web_driver.close()
    except Exception as e:
        print("Error :" + str(e))
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_Google(BaseTest):
    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"