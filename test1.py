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

T=(1,2,(33,44))
L=list(T)
print(L,type(L))