#############################################################################################################
############   To Use GMAIL Account to send mails use https://myaccount.google.com/lesssecureapps and Enable Less Secure Apps to ON.
##############################################################################################################

import os
import smtplib,ssl

smtp_server = 'smtp.gmail.com'
port = 465

sender_email = 'arundruk@gmail.com'
password = os.environ.get('my_passwd')

receiver = 'arundruk@gmail.com'
######## In the message below if you don't add To and From address, in the received mail you don't see any 'TO' Address, actually it's like mail sent to 'BCC'
message = f"""\
Subject : Hi There !!
To: {receiver}
From: {sender_email}


This message was sent from Python !!
"""

context=ssl.create_default_context()

try:
    with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver,message)

    print("Mail Sent Successfully")

except Exception as e:
    print("Sorry, Something went Wrong: "+str(e))