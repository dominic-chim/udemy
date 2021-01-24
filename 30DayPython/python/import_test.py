#from day_9 import MessageUser
from python.classes.make_messages import MessageUser

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