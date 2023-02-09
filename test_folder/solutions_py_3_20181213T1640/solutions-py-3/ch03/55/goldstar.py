## 
# Modify the program in Toolbox 3.1
# so that it adds an image (goldstar.jpg) for students with a score of at least 90 
# or a map to the tutoring center (tutoring.jpg) for those with a score of at most 50.

# Import email libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

# Define user variables
sender = "sally.smith@mycollege.edu"
username = "sallysmith"
password = input("Password: ")
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
##########################################
if score >= 90:      					 #
   file = open ("goldstar.jpg", "rb")    #
   img = MIMEImage(file.read())          #
   file.close()                          #
   msg.attach(img)  				     # attach gold star
elif score <= 50:                        #
   file = open ("tutoring.jpg", "rb")    #
   img = MIMEImage(file.read())          #
   file.close()                          #
   msg.attach(img)                       # attach map to tutoring center
##########################################
msg.attach(MIMEText(body, "plain"))

# Send off the message:
server = smtplib.SMTP(host, port)
server.starttls()
server.login(username, password)
server.send_message(msg)
server.quit()

