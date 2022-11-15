import smtplib
from email.message import EmailMessage

def alert(subject, body, to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to']=to

    user="pimessager14@gmail.com"
    msg['from']=user
    password="xxbuwfznuwmvwaqz"


    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

if __name__ == '__main__':
    alert("Hey", "Hello World", "2817866186@txt.att.net")
