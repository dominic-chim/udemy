import email
import imaplib
from re import sub
from bs4 import BeautifulSoup
import os
import mimetypes

#email
username = "devtest.dchim123@gmail.com"
password = "aUW%QDu2F8!d"

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username,password)

mail.select("inbox")


#create new folder
#mail.create("item2")

#view folders
#mail.list()

result,data = mail.uid('search',None,"ALL")

inbox_item_list = data[0].split()

for item in inbox_item_list:
    result2,email_data = mail.uid('fetch',item,'(RFC822)')
    raw_email = email_data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)
    to_ = email_message['To']
    from_ = email_message['From']
    subject_ = email_message['Subject']
    filter_subject = ""
    date_ = email_message['date'].replace(":","_")
    counter = 1

    for char in subject_:
        if char.isalnum():
            filter_subject+=char

    for part in email_message.walk():
        if part.is_multipart():
            continue
        filename = part.get_filename()
        content_type = part.get_content_type()
        if not filename:
            ext = mimetypes.guess_extension(part.get_content_type())
            if 'text' in content_type:
                ext = '.txt'
            elif "html" in content_type:
                ext = '.html'
            if not ext:
                ext = '.bin'
            filename = 'msg-part-%08d%s' %(counter,ext)
        counter+=1

        #print   
        #if "plain" in  content_type:
        #    print(part.get_payload())
        #elif "html" in content_type:
        #    html_ =  part.get_payload()
        #    soup = BeautifulSoup(html_,"lxml")
        #    text = soup.get_text()
        #    print(subject_)
        #    print(text)
        #else:
        #   print(content_type)
        
        #save
        save_path = os.path.join(os.getcwd(),"emails",date_, filter_subject)
        if not os.path.exists(save_path):
            os.makedirs(str(save_path))
        with open(os.path.join(save_path,filename), 'wb') as fp:
            fp.write(part.get_payload(decode=True))