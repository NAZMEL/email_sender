import smtplib, ssl
from config import *
from email.message import EmailMessage

# class for sending emails for each user
class Sender:
    def __init__(self, sender, password):
        self.sender_email = sender
        self.sender_password = password

    def send_mail(self, receiver_email, subject, message):
        # work server
        try:
            with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=ssl.create_default_context()) as server:
                    server.login(self.sender_email, self.sender_password)
                    for email in receiver_email:
                        #server.sendmail(self.sender_email, receiver_email, message)

                        # initialization email_message
                        msg = EmailMessage()
                        msg['Subject'] = subject
                        msg['From'] = self.sender_email
                        msg['To'] = email
                        msg.set_content(message)

                        try:
                            server.send_message(msg)
                            print(f"{bcolors.BOLD}{email}{bcolors.ENDC} {bcolors.OKGREEN}- Message was sent succesfully\n{bcolors.ENDC}")
                        except Exception as e:
                            print(f'{bcolors.FAIL}Error with {email}: {bcolors.ENDC}{bcolors.UNDERLINE}{str(e)}{bcolors.ENDC}\n')
                            

        except smtplib.SMTPException as e:
            print('Exception: ' + str(e))
