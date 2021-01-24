import csv
import datetime
import shutil
from tempfile import NamedTemporaryFile

def read_data(user_id=None, email=None):
    filename = "data.csv"
    with open(filename,"r") as csvfile:
        reader = csv.DictReader(csvfile)
        items = []
        unknown_user_id = None
        unknown_email = None
        for row in reader:
            if user_id is not None:
                if int(user_id) == int(row.get("id")):
                    return row
                else:
                    unknown_user_id = user_id
            if email is not None:
                if email == row.get("email"):
                    return row
                else:
                    unknown_email = email
        if unknown_user_id is not None:
            return "User id {user_id} not found".format(user_id=user_id)
        if unknown_email is not None:
            return "email {email} not found".format(email=email)
    return None         


def get_length(filepath):
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)

def append_data(filepath,name,email,amount):
    fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
    next_id = get_length(filepath)
    with open("data.csv","a",newline='') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        if next_id <1:
             writer.writeheader()
        writer.writerow({
            "id":next_id,
            "name":name,
            "email":email,
            "amount":amount,
            "sent":"",    
            "date": datetime.datetime.now()
            })
            
def edit_data(id = None,email = None,amount = None,sent = None):
    filename = "data.csv"
    temp_file = NamedTemporaryFile(delete=False,mode='w+', newline='')
    with open(filename, "r",) as csvfile, temp_file:
        reader = csv.DictReader(csvfile)
        fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            if id is not None:
                if int(row["id"]) == int(id):
                    row["amount"] = amount
                    row["sent"] = sent
                    print(row)
            elif email is not None and str(row["email"]) == str(email):
                row["email"] = email
                row["amount"] = amount
                row["sent"] = sent
                print(row)
            else:
                pass
            writer.writerow(row)
        temp_file.close()
        shutil.move(temp_file.name,filename)
        return True
    return False

#append_data("data.csv","Justin","testdev@test.com",123.21)
#append_data("data.csv","Bob","testdev@test.com",435)
#append_data("data.csv","Mary","testdev@test.com",56)
#append_data("data.csv","Elsa","testdev@test.com",99.99)
#append_data("data.csv","Dominic","testdev@test.com",88.88)

#edit_data(1,"othertestemail@test.com",180,True)


