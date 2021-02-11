import requests
import json

#   Client ID
#   4I0QiHrXiFnjmlUqgNyJAg
#   API Key
api_key='Bearer UoAMHv-M7vpbnydOGV8QmEohUr4g2F9mOAEb79G0sDReUSHVbJLw9FTAeMTR1Epf9oHRh3AA3zKLEondGBY964-gk1_gMJdnNBD_v27s3pddm2E0HYi3Uj6ddrISYHYx'
headers = {'Content-Type': 'application/json', 'Authorization': api_key}

search_url = 'https://api.yelp.com/v3/businesses/search'

def do_search(term='Food',location='bristol'):
    search_url = 'https://api.yelp.com/v3/businesses/search'
    term = term.replace(" ","+")
    location = location.replace(" ","+")
    url = search_url
    params = {
    "term": term,
    "location":location
    }
    r = requests.get(url,headers=headers,params=params)
    return r.json(),r.text

json_data, text_data = do_search()
python_data = json.loads(text_data)
print(json.dumps(json_data, indent=4, sort_keys=True))

for i in json_data['businesses']:
    print(i["name"])
    print(i["phone"])
    print(i["location"]["display_address"])
    print(i["location"]["city"])
