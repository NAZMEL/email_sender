PORT = "465"  # for SSL 587
SMTP_SERVER = "smtp.gmail.com"
FILE_RECEIVERS = "sources/receivers.xlsx"

SUBJECT = 'USAID TEST'
MESSAGE = """\
Hello, \n
I am writing because I think you might be interested in partnership opportunities with our company https://27n.gg/\n
27 nerds - working with Esports only! Doing tailor-made projects from scratch, also providing a full range of esports services, like betting, broadcasting, streaming.
\n
pls, advise is this smth U might be interested in?
I would appreciate your reply!
"""

# delay between a sent messages in seconds
DELAY_SEND = 30


# colors for ouptput sckripts
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'