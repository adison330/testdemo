#! /usr/bin/env python

import requests
url = "http://music.163.com/api/song/lyric?os=pc&id=411988938&lv=-1&kv=-1&tv=-1"
req = requests.get(url)
data = req.json()

#print(req)
print(data)