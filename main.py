import os
import json
from dotenv import *
import requests


#getting api token
load_dotenv
TOKEN = os.getenv('API_TOKEN')


#retriving quotes from API
def get_quote():
    #fetching resposes from a given token
    response = requests.get(TOKEN)
    #jsonify responsed data
    json_data = json.loads(response.text)
    #organising quote + author with q and a 
    quote = json_data[0]['q'] + '-' + json_data[0]['a']

    print(quote)#prints quote


#User inputs
def user_input():
    user_req = int(input("How many quotes do you want? : "))
    for i in range(user_req):
        #calls the fetching function to fetch requested amount of quotes
        get_quote()
        
#infinite user inputs
while True:
    user_input()