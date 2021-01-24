import datetime
today = datetime.date.today()
text = '{today.month}/{today.day}/{today.year}'.format(today=today)

default_names = ["Justin","john","Emily","jimbob","Andy","Ron","Harry","dominic"]
default_amounts = [123.32,94.23,123.45,675.4,43,322.457345,875,99.99]
unf_message = """Hi {name}!

Thanks for the purse on {date}, just a reminder
the puchase total is £{total}

Thanks

Dom
"""

def make_msg(names,amounts):
    messages =[]
    if len(names) == len(amounts):
        i=0
        for name in names:
            name = name[0].upper() + name[1:].lower()
            new_msg = unf_message.format(
                name=name,
                date=today,
                total="%.2f" %(amounts[i])
            )
            i+=1
            print(new_msg)

make_msg(default_names,default_amounts)