import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.co.uk/search?find_desc=Restaurants&find_loc="
loc = 'bristol'
current_page = 0

while current_page < 201:
    print(current_page)
    url = base_url + loc + "&start=" + str(current_page)
    yelp_r = requests.get(url)
    yelp_soup = BeautifulSoup(yelp_r.text, 'lxml')
    file_path = 'yelp-{loc}-2.txt'.format(loc=loc)
    with open(file_path, "a") as textfile:
        businesses = yelp_soup.findAll('div',{'class':'container__09f24__21w3G'})
        for biz in businesses:
            #print(biz)
            title = biz.findAll('div',{'class':'businessName__09f24__3Wql2'})[0].text.replace('£','')
            print(title)
            second_line = ""
            first_line = ""
            try:
                address = biz.findAll('address')[0].contents
                for item in address:
                    if "br" in str(item):
                        #print(item.getText())
                        second_line += item.getText().strip(" \n\t\r")
                    else:
                        #print(item.strip(" \n\t\r"))
                        first_line = item.strip(" \n\t\r")
                print(first_line)
                print(second_line)
            except:
                pass
            print('\n')
            try:
                catergory = biz.findAll('div',{'class':'priceCategory__09f24__2IbAM'})[0].text
            except:
                catergory = None
            print(catergory)
            page_line = "{title}\n{catergory}\n\n".format(
                    title=title,
                    address_1=first_line,
                    address_2=second_line,
                    catergory = catergory
                )
            textfile.write(page_line)
    current_page += 10


