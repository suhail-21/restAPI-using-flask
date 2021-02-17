import requests

BASE = "http://127.0.0.1:5000/"

data = [{
    "likes": 10, 
    "name": "suhail",
    "views": 3001
}, {
    "likes": 20, 
    "name": "tim",
    "views": 300123
}, {
    "likes": 298, 
    "name": "fcc",
    "views": 3456
}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)

input()
response = requests.get(BASE + "video/2")
print(response.json())