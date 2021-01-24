
from smtplib import SMTP,SMTPAuthenticationError,SMTPException #from better for third party, import for core python modules as best practice
#gmail smtp credentials
host = "smtp.gmail.com"
port = 587
username = "devtest.dchim123@gmail.com"
password = "aUW%QDu2F8!d"
wrong_pass = "wrong_password"
from_email = username
to_list = ["devtest.dchim123@gmail.com"]

email_conn = SMTP(host,port)
email_conn.ehlo()
email_conn.starttls() 
try:
    email_conn.login(username,password)
    email_conn.sendmail(from_email,to_list,"Hello World")
    print("email sent")
except SMTPAuthenticationError:
    print("Error: could not log in")
except:
    print("Error: an error occured")
email_conn.quit()



