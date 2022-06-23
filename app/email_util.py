import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def start_email_srvr():
    sender = 'admin@example.com'
    receivers = ['info@example.com']


    port = 1111
    msg = MIMEText('This is test mail')

    msg['Subject'] = 'Test mail'
    msg['From'] = 'admin@example.com'
    msg['To'] = 'info@example.com'

    with smtplib.SMTP('localhost', port) as server:
        
        # server.login('username', 'password')
        server.sendmail(sender, receivers, msg.as_string())
        print("Successfully sent email")

def send_mail(send_from, send_to, subject, text, files=None,
              server="127.0.0.1"):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)


    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

if __name__ == "__main__":
    start_email_srvr()