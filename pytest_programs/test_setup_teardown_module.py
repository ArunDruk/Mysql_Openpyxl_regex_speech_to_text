
############# Command to Generate HTML report #################
## pytest test_setup_teardown_module.py -v -s --html=google_test_report.html
###################################################

from selenium import webdriver

driver = None

def setup_module(module):
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

def teardown_module(module):
    driver.quit()

def test_google_title():
    assert driver.title == "Google"

def test_google_url():
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"
