#search all indices using elasticsearch api
import requests
import io

response = requests.get("http://127.0.0.1:9200/_cat/indices?format=json&pretty", auth=("elastic","25589rey"))
data = response.json()
for i in data:
    print(i["index"])

#create index using elasticsearch api
respone_put = requests.put("http://127.0.0.1:9200/test_index_using_api", auth=("elastic","25589rey"))
print(respone_put.text)
#search specific index using elasticsearch api
respone_get = requests.get("http://127.0.0.1:9200/test_index_using_api", auth=("elastic","25589rey"))
print("get: " +str(respone_get.json().keys()))
#create doc
url = "http://127.0.0.1:9200/"
headers = {
    "Content-Type":"application/json",
}
json_data = {
    "massage":"ghgh",
    "date":"the best day"
}
response = requests.put("http://127.0.0.1:9200/test_index_using_api/_doc/3?pretty",auth=("elastic","25589rey"),headers=headers,json=json_data)
print(response)

#get all documents in index
response_search = requests.get("http://127.0.0.1:9200/test_index_using_api/_search",auth=("elastic","25589rey"))
print(":: "+str(response_search.text))


