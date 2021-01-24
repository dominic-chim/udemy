import datetime

class MessageUser():
    user_details = []
    msgs = []
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
                self.msgs.append(new_msg)
            return self.msgs
        return []

default_names = ["Justin","john","Emily","jimbob","Andy","Ron","Harry","dominic"]
default_amounts = [123.32,94.23,123.45,675.4,43,322.457345,875,99.99]

