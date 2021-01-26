import datetime
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

class MessageUser():
    user_details = []
    msgs = []
    email_messages = []
    base_message = """Hi {name}!
Thanks for the purse on {date}, just a reminder
the puchase total is £{total}

Thanks

Dom
"""
    def add_user(self,name,amount,email=None): #setter for user details
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" %(amount)
        detail = {
            "name":name,
            "amount":amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] =date_text
        if email is not None:  #if email != None
            detail["email"] = email
        self.user_details.append(detail)
    def get_details(self): # getter for list of user details
        return self.user_details
    def make_message(self):
        if len( self.user_details ) >0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                user_email = detail.get("email")
                if user_email:
                    user_data = {
                        "email": user_email,
                        "message": new_msg
                    }
                    self.email_messages.append(user_data)
                self.msgs.append(new_msg)
            return self.msgs
        return []
    def send_email(self):
        self.make_message()
        if len(self.email_messages) >0:
            
            for detail in self.email_messages:
                try:
                    email_conn = SMTP(host,port)
                    email_conn.ehlo()
                    email_conn.starttls() 
                    email_conn.login(username,password)
                except SMTPAuthenticationError:
                    print("Error: could not log in")
                    
                user_email = detail['email']
                user_message = detail['message']
                #run email
                the_msg = MIMEMultipart("alternative")
                the_msg['Subject'] = "Hello There"
                the_msg['From'] = from_email
                the_msg['To'] = user_email
                part_1 = MIMEText(user_message, 'plain')
                the_msg.attach(part_1)
                #the_msg.attach(part_2)
                try:
                    email_conn.sendmail(from_email,to_list,the_msg.as_string())
                    print("email sent to " + user_email)
                except:
                    print("Error: an error occured")
            email_conn.quit()
            return True
        return False

obj = MessageUser()
obj.add_user("Justin",123.32,email = 'devtest.dchim123@gmail.com')
obj.add_user("john",94.23,email = 'devtest.dchim123@gmail.com')
obj.add_user("Emily",123.45,email = 'devtest.dchim123@gmail.com')
obj.add_user("jimbob",675.4,email = 'devtest.dchim123@gmail.com')
obj.add_user("Andy",42,email = 'devtest.dchim123@gmail.com')
obj.add_user("Rong",322.457345,email = 'devtest.dchim123@gmail.com')
#print(obj.get_details())
#print(obj.make_message())
obj.send_email()