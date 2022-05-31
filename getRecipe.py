import requests
import credentials  

querystring  = {"from":"0",
                "size":"20",
                "tags":"under_30_minutes"}


response = requests.get("https://tasty.p.rapidapi.com/recipes/list" , headers = credentials.headers, params = querystring )



receipes = response.json()


print (receipes)