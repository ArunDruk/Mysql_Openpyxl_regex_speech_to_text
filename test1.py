##############################################################################################################
# Name Mapping and login using Test Complete
# def Test1():
#   Browsers.Item[btChrome].Run("http://www.webmail.testyantra.in/")
#   browser = Aliases.browser
#   browser.ToUrl("http://webmail.testyantra.in/")
#   page = browser.pageWebmailLogin
#   textbox = page.formLoginForm.textboxEmailAddress
#   textbox.Click(30, 18)
#   page.textboxEmailAddress.SetText("ar")
#   textbox.Keys("[Down][Enter][Tab]")
#   page.passwordboxPassword.SetText("Feb@2020")
#   page.buttonLogIn.ClickButton()
#   browser.pageIndex.Wait()
##############################################################################################################

# import configparser
#
# config=configparser.ConfigParser()
# config.read("Setting.ini")
# Name=config.get("ebiz","usrid")
# print(Name)
#
# passwd=config.get("ebiz","pswd")
# print(passwd)
#
# print(config["ebiz"]["url"])
# print(config["ebiz"])
#
# config.set("ebiz","user","akumar6")

##############################################################################################################

payload = {
         "customerDetails" : {
         "soldToCustomerNumber" : "5000871",
         "billToCustomerNumber" : "",
         "includeBasicFloorplans" : "FALSE",
         "vehicleAttributes" : [ {
         "vehicleReferenceId" : "7037088",
         "vehicleYear" : "2018",
         "maxOdometerReading" : "120",
         "asIsIndicator" : "FALSE",
         "totalVehicleDebitAmount" : "1000",
         "salvageUnitIndicator" : "FALSE",
         "salesChannel" : "RMS",
         "vehicleType" : "V",
         "saleType" : "O",
         "hondaFloorplanThresholdFlag" : "TRUE",
         "sellerAccount" : ""
         }
         ]
         }
         }

L=payload["customerDetails"]["vehicleAttributes"]
print(L[0]["vehicleReferenceId"])

print(payload["customerDetails"]["vehicleAttributes"][0]["maxOdometerReading"])

L1=payload["customerDetails"]["soldToCustomerNumber"]
print(L1)