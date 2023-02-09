## 
# Modify the program in Toolbox 3.1 
# to prompt whether to attach a file to the message. 
# If so, prompt for the file location and attach it.

# Import email libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib

# Define user variables
sender = "sally.smith@mycollege.edu"
username = "sallysmith"
password = input("Password: ")
addfile = ""
if input("Would you like to attach a file? Y or N?")== "Y":
    addfile = input("  Please enter filename => ")
host = "smtp.myserver.com"
port = 587

# Prompt for the recipient’s e-mail address and test score.
# Create a message body depending on the score.
recipient = input("Student email: ")
score = int(input("Score: "))
body = "Your score on the last exam is " + str(score) + ". \n" 
if score <= 50 :
    body += "To do better next time, why not visit the tutoring center?"
elif score >= 90 :
    body += "Fantastic job! Keep it up."
    
# Assemble the message. 
msg = MIMEMultipart()
msg.add_header("From", sender)
msg.add_header("To", recipient)
msg.add_header("Subject", "Exam score")
##############################
if addfile != "":            
   fp = open (addfile, "rb") 
   attachment = MIMEApplication(fp.read())
   fp.close()
   attachment.add_header("Content-Disposition", "attachment; filename=" + addfile)
   msg.attach(attachment)    # attach file
##############################

msg.attach(MIMEText(body, "plain"))

# Send off the message:
server = smtplib.SMTP(host, port)
server.starttls()
server.login(username, password)
server.send_message(msg)
server.quit()

