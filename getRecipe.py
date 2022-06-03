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

idNumber =  context['recipes'][0]['id']
name = context['recipes'][0]['title']
timeToPrepare = context['recipes'][0]['readyInMinutes']
isVegetarian = context['recipes'][0]['vegetarian']
isVegan = context['recipes'][0]['vegan']
isGlutenFree = context['recipes'][0]['glutenFree']
isDairyFree = context['recipes'][0]['dairyFree']
instructions = context['recipes'][0]['instructions']
url = context['recipes'][0]['sourceUrl']
servings = context['recipes'][0]['servings']

listOfIngredeitns = []

instructions = instructions.replace("</li><li>", "\n\n")
instructions = instructions.replace ("<ol><li>", "")
instructions = instructions.replace ("</li></ol>","")

print (f"""Here is your random dish suggestion:

----{name}----

The time to prepare this dish is:  {timeToPrepare}

Additional information:

Is it:
vegetarian? : {isVegetarian}
vegan? : {isVegan}
gluten free? : {isGlutenFree}
dairy free? : {isDairyFree}


""")

while True:
    decision = input ("Would you like to check list of ingredeitns and receipe? Yes/No: ")
    if (decision.upper() == 'YES'):
        print ("""

-------List of ingredeitns:-------    
        """)
        for ingredeitns in context['recipes'][0]['extendedIngredients']:
            for key, value in ingredeitns.items():
                if (key == 'original'):
                    print (value)
                    listOfIngredeitns.append(value)
        print (f"""

------- How to prepare? -------

{instructions}
        
        
        """)
        decisionToSave = input ('Would you like to add this receipe to a file with your favoritues? Yes/No: ')
        if (decisionToSave.upper() == 'YES'):
            # a file with information about your saved dishes will be created
            with open ("myFavoritueMeals","a+", encoding = "Utf-8") as file:
                file.write("id: ")
                file.write (str(idNumber))
                file.write("\nname: ")
                file.write (name)
        break
    elif (decision.upper() == 'NO'):
        break
    else:
        print ('Wrong input')


