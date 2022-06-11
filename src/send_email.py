from email.mime.text import MIMEText
import smtplib

def send_email(name, surname, email, height, age, shoesize, avg_height, avg_shoesize):
    from_email = "jeglaverlortiden@gmail.com"
    from_password="wqhrjhswfdtjwzmo"

    to_email = email
    subject="SurveyApply"
    message = "Hello <strong>%s</strong> <strong>%s</strong>!<br><br> Thank you for participating  in this survey. Here is your results. <br> Your heigth is <strong>%s</strong> and you are <strong>%s</strong> years old and you use <strong>%s</strong> in shoesize.<br>The average height is %s, and the average shoesize is %s.<br><br> Sincerely, SurveyApply" %(name, surname, height, age, shoesize, avg_height, avg_shoesize)

    msg = MIMEText(message,'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['from']=from_email

    gmail = smtplib.SMTP('smtp.gmail.com',587 )
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)

