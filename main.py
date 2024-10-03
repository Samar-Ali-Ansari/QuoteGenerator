#imports 
import json
import requests

#retriving quotes from API
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + '-' + json_data[0]['a']
    print("-----------")
    print(quote)
    print("-----------")

#User inputs
def user_input():
    user = int(input("How many quotes do you want? : "))
    for i in range(user):
        get_quote()
        
#infinite user inputs
while True:
    user_input()
