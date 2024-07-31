import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Email setup
SMTP_SERVER = 'smtp.gmail.com'  # SMTP server for Gmail
SMTP_PORT = 587  # Typically 587 for TLS, 465 for SSL
EMAIL_ADDRESS = ''  # Sender's email
EMAIL_PASSWORD = ''  # Sender's email password

# Email content setup
RECIPIENT_EMAIL = 'commonimperative@gmail.com'  # Recipient's email
SUBJECT = 'MobileIPS Daily Report'
BODY = 'This is your daily report.\n\nBest Regards,\nYour Automated System'

def send_email():
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = SUBJECT
    msg.attach(MIMEText(BODY, 'plain'))

    # Connect to the server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Secure the connection
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, text)
    server.quit()
    print("Email sent successfully")

# Schedule the email sending
schedule.every().day.at("15:55").do(send_email)

# Main loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)


