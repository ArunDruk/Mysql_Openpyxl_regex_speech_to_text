from selenium import webdriver
from configparser import ConfigParser
import time
import win32com.client as win32
from webdriver_manager.chrome import ChromeDriverManager

parser= ConfigParser()
parser.read('conf.ini')
url = parser.get('Settings','URL')
goods = parser.get('Settings', 'Goods')
to_address = parser.get('Settings', 'Email Address To')
cc_address= parser.get('Settings', 'Email Address Cc')


driver=webdriver.Chrome(ChromeDriverManager().install())
# driver=webdriver.Chrome()
driver.get(url)
time.sleep(5)

if goods.lower() == "sensex":
    xpath="//*[@id='home_page_widget_db_data_inc']/div/div[1]/a/div[2]"
elif goods.lower() == "nifty":
    xpath = "//*[@id='home_page_widget_db_data_inc']/div/div[2]/a/div[2]"
elif goods.lower() == "gold":
    xpath = "//*[@id='home_page_widget_db_data_inc']/div/div[3]/a/div[2]"
elif goods.lower() == "silver":
    xpath = "//*[@id='home_page_widget_db_data_inc']/div/div[4]/a/div[2]"
elif goods.lower() == "petrol":
    xpath = "//*[@id='home_page_widget_db_data_inc']/div/div[5]/a/div[2]"
elif goods.lower() == "diesel":
    xpath = "//*[@id='home_page_widget_db_data_inc']/div/div[6]/a/div[2]"
elif goods.lower() == "usd":
    xpath = "//*[@id='home_page_widget_db_data_inc']/div/div[7]/a/div[2]"

value = driver.find_element_by_xpath(xpath)
price=value.text

time.sleep(5)
driver.quit()
########### Below code is to send the Email via Outlook #######################

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = to_address
mail.CC = cc_address
mail.Subject = f"Today's {goods} value/price"
mail.Body = f"""Hi,

	Today’s {goods} value/price is : {price}

Thank you.
Automation Team
"""

mail.Send()
