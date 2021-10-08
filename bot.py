#Imports
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook
import requests


#Global Variables
url = "https://api.coincap.io/v2/assets"
wb = Workbook()
ws = wb.active
tracked_currencies = ['bitcoin', 'ethereum']
# hourly = f"https://api.coincap.io/v2/assets/{}/history?interval=h1"
budget = ...

#Functions

def get_data():
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()['data']
        export = []
        for n in range(len(data)):
            for target in tracked_currencies:
                currency = data[n]['id']
                if target == currency:
                    price = data[n]['priceUsd']
                    pair = (currency, price)
                    export.append(pair)
        return export
    else:
        return f"something went wrong! Error - {str(resp.status_code)}"

def daily_check():
    export = []
    for target in tracked_currencies:
        daily = f"https://api.coincap.io/v2/assets/{target}/history?interval=d1"
        resp = requests.get(daily)
        if resp.status_code == 200:
            data = resp.json()['data']
            for n in range(len(data)):
                currency = target
                price = data[n]['priceUsd']
                pair = (currency, price)
                export.append(pair)
        else:
            return f"something went wrong! Error - {str(resp.status_code)}"
    return export

def hourly_check():
    export = []
    for target in tracked_currencies:
        hourly = f"https://api.coincap.io/v2/assets/{target}/history?interval=h1"
        resp = requests.get(hourly)
        if resp.status_code == 200:
            data = resp.json()['data']
            for n in range(len(data)):
                currency = target
                price = data[n]['priceUsd']
                pair = (currency, price)
                export.append(pair)
        else:
            return f"something went wrong! Error - {str(resp.status_code)}"
    return export

def write_data():
    pass

#Main Loop
print(daily_check())
