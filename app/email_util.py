import yagmail

user = 'vidfanbooth@gmail.com'
app_password = 'jepw jzhj uekr pqsk' # a token for gmail

subject = 'Fan Booth Video'
content = ['Here is you video!'] # todo add attachment


def send_email(to, attachment=" Video to be sent."):
    content.append(attachment)
    
    with yagmail.SMTP(user, app_password) as yag:
        yag.send(to, subject, content)
        print('Sent email successfully')
        
if __name__ == "__main__":
    send_email("Jerryshi1016@gmail.com", "hi")