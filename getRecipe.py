import requests
import credentials
# credentials is a file where you should put your X-RapidAPI-Key and X-RapidAPI-Host 
# you can take it from https://spoonacular.com/food-api

import json



def get_your_receipes ():

    querystring  = {
                "limitLicense":True,
                "number	":"1",
                
                }

    response = requests.get("https://api.spoonacular.com/recipes/random" , headers = credentials.headers, params = querystring )

    return get_json_content_from_responde (response)

def get_json_content_from_responde (response):
    try:
        context = response.json ()
    except json.decoder.JSONDecodeError:
        print ('bledny format')
    else:
        return context



context = get_your_receipes()

name = context['recipes'][0]['title']
timeToPrepare = (context['recipes'][0]['readyInMinutes'])

print (f""" Here is your random dish suggestion:

{name}

The time to prepare this dish is:  {timeToPrepare}

""")




print(context['recipes'][0]['servings'])
print(context['recipes'][0]['sourceUrl'])


for ingredeitns in context['recipes'][0]['extendedIngredients']:
    for key, value in ingredeitns.items():
        if (key == 'original'):
            print (value)
