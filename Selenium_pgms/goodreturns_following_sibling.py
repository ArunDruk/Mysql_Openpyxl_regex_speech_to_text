from selenium import webdriver
import time

driver=webdriver.Chrome()
url="http://www.goodreturns.in"
driver.get(url)

time.sleep(4)


############################# Generic XPATH for Gold, Silver, Petrol, Diesel, USD ###########################################################
# Below Xpath will work for goods = 'Petrol', 'Diesel',
goods=["Gold","Silver","Petrol","Diesel","USD"]

for i in goods:
    price_obj=driver.find_element_by_xpath(f"//div[contains(text(),'{i}')]/following-sibling::div[@class = 'gr-home-widget-block-price gr-clearfix']/span")
    print(f"Today's {i} value is: " +price_obj.text)
############################################# Xpath for Sensex and Nifty #################################################################
# Below Xpath will work for goods = 'Nifty', 'Sensex'

goods=["Sensex","Nifty"]
for i in goods:
    price_obj=driver.find_element_by_xpath(f"//div[contains(text(),'{i}')]/following-sibling::div") # This will display Today's Up or Down value.
    today_stock_market_obj=driver.find_element_by_xpath(f"//div[contains(text(),'{i}')]")
    print("Today's Stock Market value: " +today_stock_market_obj.text)
    print("Today's Change: " + price_obj.text)
##############################################################################################################

time.sleep(5)
driver.quit()