## 
# Modify the program in Toolbox 3.1
# so that it "blind copies" the tutoring lab for students in need of tutoring.
# Provide the address of the lab as a constant string in your program.

# Import email libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Define user variables
sender = "sally.smith@mycollege.edu"
username = "sallysmith"
password = input("Password: ")
host = "smtp.myserver.com"
port = 587
TUTOR_LAB = "tutoring-lab@mycollege.edu"

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
#########################################################
if score <= 50 :					  # If score is low,
	msg.add_header("Bcc", TUTOR_LAB)  # blind copy tutoring lab.
#########################################################
msg.attach(MIMEText(body, "plain"))

# Send off the message:
server = smtplib.SMTP(host, port)
server.starttls()
server.login(username, password)
server.send_message(msg)
server.quit()

