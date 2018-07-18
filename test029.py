#! /usr/bin/env python

import requests
url = "http://music.163.com/api/playlist/detail?id=402614161"
req = requests.get(url)
data = req.json()

print(req)
print(data)