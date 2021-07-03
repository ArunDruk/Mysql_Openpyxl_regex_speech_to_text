### Creating Global Pytest fixture using Conftest.py file (configuration test file)
# The methods or the fixtures present in conftest.py can be used for all the different test files and methods, it is like globally we are declaring it.
# you can use multiple methods in conftest.py file

from pytest import fixture
from pytest import mark

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# @pytest.fixture(params=["chrome","firefox"],scope='class')
# def init_driver(request):
#     if request.param == 'chrome':
#         web_driver = webdriver.Chrome(ChromeDriverManager().install())
#     if request.param == 'firefox':
#         web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     request.cls.driver = web_driver
#     web_driver.implicitly_wait(10)
#     yield
#     web_driver.close()
@fixture(scope="session")
def chrome_browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.close()
