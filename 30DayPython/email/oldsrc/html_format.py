
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP,SMTPAuthenticationError,SMTPException #from better for third party, import for core python modules as best practice
#gmail smtp credentials

host = "smtp.gmail.com"
port = 587
username = "devtest.dchim123@gmail.com"
password = "aUW%QDu2F8!d"
wrong_pass = "wrong_password"
from_email = username
to_list = ["devtest.dchim123@gmail.com"]

try:
    email_conn = SMTP(host,port)
    email_conn.ehlo()
    email_conn.starttls() 
    the_msg = MIMEMultipart("alternative")
    the_msg['Subject'] = "Hello There"
    the_msg['From'] = from_email
    plain_txt = "Testing the message"
    html = """ \
    <html>
        <head></head>
        <body>
            <p> Hey! <br>
                Testing this email <b>message</b>. Made by <a href='http://joincfe.com'>Team CFE</a>.
            </p>
        </body>
    </html>
    """
    part_1 = MIMEText(plain_txt, 'plain')
    part_2 = MIMEText(html, "html")
    the_msg.attach(part_1)
    the_msg.attach(part_2)

    try:
        email_conn.login(username,password)
        email_conn.sendmail(from_email,to_list,the_msg.as_string())
        print("email sent")
    except SMTPAuthenticationError:
        print("Error: could not log in")
    email_conn.quit()
except:
    print("Error: an error occured")