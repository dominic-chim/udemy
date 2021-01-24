class Animal():
    noise = "Grunt"
    size = "Large"
    colour = "Brown"
    hair = "Covers body"
    def get_colour(self,abc):
        return self.colour + " " + abc
    @property
    def make_noise(self):
        return self.noise

class Dog(Animal):
    name = 'Jon'
    colour = 'Black'
    noise = "Bark"
    hair = "hairless"
    size = "Small"
    age = 5

dog = Animal()
dog.get_colour("red")

#arg = positinal arguments
#kwarg = Keyword argument
#ordering arg first then kwarg
def func(arg1,arg2,kwarg1=None,kwarg=None):
    print(arg1,arg2)
    if kwarg1 != None:
        print(kwarg1)
    pass

func("abc","car",kwarg1='Not a big deal') 


email_address = "test@test.com"
to_list = ["abc@gmail.com"]
from_list = ["another2@gmail.com","test2@test.com"]

def send_email(email_address=email_address,to_list=to_list,from_list=from_list):
    pass
send_email(email_address=email_address,to_list=to_list,from_list=from_list)