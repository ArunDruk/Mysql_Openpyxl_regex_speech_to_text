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

#################### Accessing the values inside the Dictionary of Dictionary ###########################


# payload = {
#          "customerDetails" : {
#          "soldToCustomerNumber" : "5000871",
#          "billToCustomerNumber" : "",
#          "includeBasicFloorplans" : "FALSE",
#          "vehicleAttributes" : [ {
#          "vehicleReferenceId" : "7037088",
#          "vehicleYear" : "2018",
#          "maxOdometerReading" : "120",
#          "asIsIndicator" : "FALSE",
#          "totalVehicleDebitAmount" : "1000",
#          "salvageUnitIndicator" : "FALSE",
#          "salesChannel" : "RMS",
#          "vehicleType" : "V",
#          "saleType" : "O",
#          "hondaFloorplanThresholdFlag" : "TRUE",
#          "sellerAccount" : ""
#          }
#          ]
#          }
#          }
# print(payload.keys())

#
# L=payload["customerDetails"]["vehicleAttributes"]

# print(L[0]["vehicleReferenceId"])
#
# print(payload["customerDetails"]["vehicleAttributes"][0]["maxOdometerReading"])
#
# L1=payload["customerDetails"]["soldToCustomerNumber"]
# print(L1)
####################################################################################################

# def add():
#     print("Hello")
#     return 2
#
# a=["add()"]
# print(a)

# x=[1,2,3,4,5,6]
# print(x[0:-3])

#x=["th3yr","rew8","6pore"]
##############################################################################
# x="th3yrr6ew8pore"
#
# a="".join(i for i in x if i.isdigit())
# print(a)

##############################################################################

# L=["tc107132is_us_ap_costar_invoice_import_request_set()"]
# print(L[0])
##############################################################################################################
# a=3
# if not a:
#     print("Pass")
# else:
#     print("fail")

##############################################################################################################
# class func1():
#     def add(self):
#         return 2
#
#     def sub(self):
#         return 3
#
#     def mul(self):
#         return 4
#
# class func2():
#     def div(self):
#         return 5
#
#     def alt(self):
#         return 6
#
#     def mul(self):
#         pass