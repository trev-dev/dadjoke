#! /usr/bin/python
from urllib import request
import json

url = 'http://icanhazdadjoke.com'
headers = {
    'User-Agent': (
        'Mozilla/5.0 (X11; Linux i686; rv:80.0) Gecko/20100101 Firefox/80.0'
    ),
    'Accept': 'application/json'
}

req = request.Request(url, data=None, headers=headers)
with request.urlopen(req) as response:
    data = response.read()

joke = json.loads(data)['joke']
print(joke)
