from selenium import webdriver
import time

driver=webdriver.Chrome()

# url="http://demo.guru99.com/test/guru99home/"
# url="http://www.goodreturns.in"
url="https://developer.salesforce.com/"
driver.get(url)
time.sleep(5)
L1=[]
######################################################################### Below need to use the URL guru99.com #############################################################################
# elements=driver.find_elements_by_xpath("//h2[contains(text(),'A few of our most popular courses')]/parent::div//div[//a[contains(text(),'SELENIUM')]]/following-sibling::div[@class='rt-grid-2 rt-omega']")
###################################################################################################################################################################################################
######################################################################### Below need to use the URL goodreturns.in #########################################################################
# elements=driver.find_elements_by_xpath("//div[@id='home_page_widget_db_data_inc']/parent::div//div[//a[contains(text(),'Gold')]]/following-sibling::div[@class='gr-home-widget-block']")

#########################################################################Below need to use the URL salesforce.com #########################################################################
# elements=driver.find_elements_by_xpath("//ul[@class = 'nav primary-nav clearfix']") # Heading classification
# elements =driver.find_elements_by_xpath("//h3[contains(text(),'Developer Centers')]/following-sibling::ul")  # Footer itmes inside Developer Centers
# driver.find_element_by_css_selector("input#first_name").send_keys("ArunDruk") # using CSS Selector for the developer salesforce Sign-up

elements=driver.find_elements_by_xpath("//h2[contains(text(),'Check out our newest courses')]/parent::div//div[//a[contains(text(),'VBScript')]]//preceding-sibling::div[@class='rt-grid-2 rt-omega']")

for ele in elements:
    price=ele.text
    # print(price)
    L1.append(price)

for i in L1:
    print(i)

time.sleep(4)
driver.quit()

