from sender import Sender
from config import *
from excel import Excel_work

sender = 'open.cv18@gmail.com'     #change it
password = "open.cv18ukr1"        #change it

if __name__ == '__main__':
    
    # getting all emails from excel file
    file = Excel_work(FILE_RECEIVERS)
    emails = file.get_emails()
    
    # sending emails with class Sender
    try:
        Sender(sender, password).send_mail(emails, SUBJECT, MESSAGE)
    except Exception as e:
        print(f'{bcolors.WARNING} Global Error:{bcolors.ENDC} {bcolors.FAIL}{str(e)}{bcolors.ENDC}')




                