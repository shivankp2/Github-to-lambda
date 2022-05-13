# import libraries here

import pandas

from botocore.vendored import requests

from datetime import datetime

def lambda_handler(event, context):
    now = datetime.now()
    now_str = now.strftime(‘%Y-%m-%d %H:%M:%S’)

    response = requests.get(‘https://newsapi.org/v2/everything?q=tesla&from=2022-05-07&sortBy=publishedAt&apiKey=590a0141d1e44a268a21f6bb6c39d5ea′)

    if response.status_code == 200:
        datadictionary = response.json()

    for data in datadictionary[‘list’]:
        source = articles['name']
        author = articles['author']
        title = articles['title']
        publishedAt = articles['publishedAt']

    print(f."Name:{name}, author :{author}, title : {title}, publishedAt:{publishedAt}")
    return "Name:{}, author :{}, title : {}, publishedAt:{}".format(name,author,title,publishedAt))