from elasticsearch import Elasticsearch
import io

ELASTIC_PASSWORD = "25589rey"

es=Elasticsearch(
    "http://127.0.0.1:9200",
    basic_auth=("elastic", ELASTIC_PASSWORD))
print(es.ping())
es.indices.create(index="red2")
indice = es.indices.get(index="*")
for index in indice:
    print(index)

with io.open("logs.txt","r",encoding="utf-8") as file1:
    data = file1.read()
    file1.close()
print(data)

#search specific index
#index_spec = "red1"
#search index based on pattern
"""
index_spec = "red*"
try:
    response = es.search(index=index_spec)
    print(response)
except Exception as e:
    print(str(e))
    """
#search and display the index names based on the given search pattern
index_spec = "red*"
response = es.indices.get_alias(index=index_spec)
print(len(response))
#delete index
for i in response:
    del_res = es.indices.delete(index=i)
    print(i + " deleted")
es.indices.create(index="red2")
es.indices.create(index="red1")
es.indices.create(index="red3")



    