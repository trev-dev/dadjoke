#! /usr/bin/python
import requests

joke = requests.get('https://icanhazdadjoke.com', headers={"Accept": "application/json"})

try:
    print(joke.json()['joke'])
except e:
    pass
