##############################################################################################################
############   To Use GMAIL Account to send mails use https://myaccount.google.com/lesssecureapps and Enable Less Secure Apps to ON.
##############################################################################################################
######## If still facing issue Try this https://accounts.google.com/DisplayUnlockCaptcha  ###########

# the first step is always the same: import all necessary components:
import smtplib,ssl
from socket import gaierror
import os

# now you can play with your code. Let’s define the SMTP server separately here:
port = 587  # 465
smtp_server = "smtp.gmail.com"
# login = "1a2b3c4d5e6f7g"
password = os.environ.get("my_passwd")

# specify the sender’s and receiver’s email addresses
sender_email = "arundruk@gmail.com"
receiver_email = "arundruk@gmail.com"

# type your message: use two newlines (\n) to separate the subject from the message body, and use 'f' to  automatically insert variables in the text
######## In the message below if you don't add To and From address, in the received mail you don't see any 'TO' Address, actually it's like mail sent to 'BCC'
message = f"""\
Subject: Hi Mailtrap
To: {receiver_email}
From: {sender_email}

This is my first message with Python."""
context = ssl.create_default_context()
try:
    #send your message with credentials specified above
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    # tell the script to report if your message was sent or which errors need to be fixed
    print('Mail Sent Successfully')
except (gaierror, ConnectionRefusedError):
    print('Failed to connect to the server. Bad connection settings?')
except smtplib.SMTPServerDisconnected:
    print('Failed to connect to the server. Wrong user/password?')
except smtplib.SMTPException as e:
    print('SMTP error occurred: ' + str(e))