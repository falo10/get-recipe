import requests
# credentials is a file where you should put your X-RapidAPI-Key and X-RapidAPI-Host 
# you can take it from https://rapidapi.com/apidojo/api/tasty/
import credentials
import json

def get_your_receipes ():

    querystring  = {
                "from":"0",
                "size":"1",
                "tags":"under_30_minutes"
                }

    response = requests.get("https://tasty.p.rapidapi.com/recipes/list" , headers = credentials.headers, params = querystring )

    return get_json_content_from_responde (response)

def get_json_content_from_responde (response):
    try:
        context = response.json ()
    except json.decoder.JSONDecodeError:
        print ('bledny format')
    else:
        return context

results = get_your_receipes()
print (results)