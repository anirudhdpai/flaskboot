import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "Day", "views": 100545, "likes": 910},
{"name": "Life 1", "views": 10045, "likes": 10},
{"name": "Software 2", "views": 90545, "likes": 100}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/1")
print(response.json())
