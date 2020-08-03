import requests
import pdb

print("EXAMPLE OF GET API CALL")  
GET_URL = "https://postman-echo.com/get"
GET_PARAMS = {'foo1':"bar1", "foo2":"bar2"} 

resp1 = requests.get(url=GET_URL, params=GET_PARAMS)
respjson1 = resp1.json()

print(respjson1["url"])
if(len(respjson1["args"]) > 0):
        print(respjson1["args"]["foo1"])
        print(respjson1["args"]["foo2"])

print("EXAMPLE OF POST API CALL")  
POST_URL = "https://postman-echo.com/post"
POST_DATA = {'foo1':"bar1", 'foo2':'bar2'}

resp2 = requests.post(url=POST_URL, data=POST_DATA)
respjson2 = resp2.json()

print(respjson2["url"])
print(respjson2["form"])


print("EXAMPLE OF PUT API CALL")  
PUT_URL = "https://postman-echo.com/put"
PUT_DATA = {'foo1':"bar1", 'foo2':'bar2'}

resp3 = requests.put(url=PUT_URL, data=PUT_DATA)
respjson3 = resp3.json()

print(respjson3["url"])
print(respjson3["form"])