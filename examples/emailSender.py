import smtplib
to = input("Enter the Email to the Recipient")
content = input("Enter the content of the Email")
senderEmail = "senderEmail@gmail.com"

# 
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(senderEmail, "YOUR-PASSWORD")  # user + password or your email
    server.sendmail(senderEmail, to, content)
    server.close()


sendEmail(to, content)
