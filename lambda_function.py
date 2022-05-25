import requests
from datetime import datetime

def lambda_handler(event, context):
    now = datetime.now()
    response = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2022-05-09&to=2022-05-23&sortBy=publishedAt&apiKey=590a0141d1e44a268a21f6bb6c39d5ea')
    if response.status_code==200:
        datadictionary=response.json()
        
    return datadictionary['articles']