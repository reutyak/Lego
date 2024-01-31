import requests
import io

with io.open("9.csv","r",encoding="utf-8") as f1:
    data = f1.read()
    f1.close()
lines= data.split("\n")[1:]
i = 1
for line in lines:
    print(line)
    id_case = line.split(",")
    print(len(id_case))
    #activity = line.split(",")[1]
    #time = line.split(",")[2]
    url = "http://127.0.0.1:9200/"
    headers = {
        "Content-Type":"application/json",
    }
    json_data = {
        "id case":id_case,
        #"activity":activity,
        #"timestamp":time
    }
    response = requests.put(url+f"test_index_using_api/_doc/{i}?pretty",headers=headers,json=json_data,auth=("elastic","25589rey"))
    i+=1