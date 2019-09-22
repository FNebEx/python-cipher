import smtplib

def sendMessage(from_email, to_email, password, message):
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(from_email, password)
    session.sendmail(from_email, to_email, message)
    session.quit()