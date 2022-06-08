import requests
import credentials
# credentials is a file where you should put your X-RapidAPI-Key
# you can take it from https://spoonacular.com/food-api
import json
from enum import *



def get_your_recipes ():

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

def get_your_favourite_recipes (idNumber):
    
    querystring  = {
                "id":idNumber
                }

    response = requests.get("https://api.spoonacular.com/recipes/random" , headers = credentials.headers, params = querystring )

    return get_json_content_from_responde (response)

def check_your_favourites_dishes (fileName):
    with open (fileName, "r+", encoding = "Utf-8") as file:
        file.seek(0)
        print (file.read())

Options = Enum ('Options',{ 'random': 'random',
                            'favoritue':'favoritue',
                            'receipe': 'receipe',
                            'exit': 'exit'})

print('Welcome to GET RECIPE 1.0 powered by falo10 :)')

while True:

    selectedOption = input(f""" Write:

    "random" - to receive proposition of random receipe
    "favoritue" - to check names and IDs of your favoritue dishh (if you already have one!)
    "receipe" - if you want to check receipe of some specific dish (you will have to provide ID number of that dish)
    "exit" - if you want to exit the program

    """)


#option 0 check your file with favourite meals (the file will be created after you will add some dish to favoritues!)
    
    if (selectedOption == Options.favoritue.value):

        check_your_favourites_dishes("myFavouriteMeals.txt")
        continue

# option 1 - get your receipe
    elif (selectedOption == Options.receipe.value):
    

        idOfFavouriteMeal = int(input("Wirte id number of one of your favourite meals, that you want to "))

        contextOfFavourite = get_your_favourite_recipes (idOfFavouriteMeal)

        instructionsOfFavourite = contextOfFavourite['recipes'][0]['instructions']
        instructionsOfFavourite = instructionsOfFavourite.replace("</li><li>", "\n\n")
        instructionsOfFavourite = instructionsOfFavourite.replace ("<ol><li>", "")
        instructionsOfFavourite = instructionsOfFavourite.replace ("</li></ol>","")
        print ("""

        -------List of ingredeitns:-------    
                """)
        for ingredeitns in contextOfFavourite['recipes'][0]['extendedIngredients']:
            for key, value in ingredeitns.items():
                if (key == 'original'):
                    print (value)
        print( f""")
        ------- How to prepare? -------

        {instructionsOfFavourite}
                
                
                """)
        continue

    # option2 - get random recipe
    elif (selectedOption == Options.random.value):

        context = get_your_recipes()

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
                            print (value),
                print (f"""

        ------- How to prepare? -------

        {instructions}
                
                
                """)
                decisionToSave = input ('Would you like to add this receipe to a file with your favourites? Yes/No: ')
                if (decisionToSave.upper() == 'YES'):
                    # a file named "myFavouritesMeals" with information about your favourite dishes will be created
                    with open ("myFavouriteMeals.txt","a+", encoding = "Utf-8") as file:
                        file.write ("\n")
                        file.write("id: ")
                        file.write (str(idNumber))
                        file.write("\nname: ")
                        file.write (name)
                        
                break
            elif (decision.upper() == 'NO'):
                break
            else:
                print ('Wrong input')
        continue

    elif (selectedOption == Options.exit.value):
        break

    else:
        print("""
        Invalid input! Try again.
        """)
        continue


print ('Thank you for using GET RECIPE! See you next time! ')