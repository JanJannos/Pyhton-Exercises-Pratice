import requests
from win10toast import ToastNotifier
import json
import time


def update():
    req = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    data = req.json()
    text = f'Confirmed Cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered: {data["recovered"]}'

    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid-19 Updated", text, duration=20)
        time.sleep(60)


update()
