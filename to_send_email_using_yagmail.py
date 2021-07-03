
###############################  pip install yagmail ####################
############################ pip install keyring ############################

import yagmail

receiver = "arundruk@gmail.com"
body = "Hello there from Yagmail"
filename = "QR_image1.png"

yag = yagmail.SMTP("arundruk@gmail.com")
try:
    yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body,
    attachments=filename,
    )
    print("Mail Sent Successfully")
except Exception as e:
    print("Sorry some error occurred : " + e)
