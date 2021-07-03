import configparser

config=configparser.ConfigParser()
config.read("Setting.ini")
Name=config.get("ebiz","usrid")
print(Name)

passwd=config.get("ebiz","pswd")
print(passwd)

print(config["ebiz"]["url"])
print(config["ebiz"])

config.set("ebiz","usrid","akumar6")
print(Name)