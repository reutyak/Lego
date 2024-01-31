from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from datetime import datetime
import csv

ELASTIC_PASSWORD = "25589rey"

index = "trydata"

client = Elasticsearch(
    "http://127.0.0.1:9200",
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

data = {
    "name" : "miri",
    "last_name": "glik",
    "city": "bneybrak",
    "date": datetime.now()
}

client.index(index = index , body = data)

with open("9.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    bulk(client, reader, index = index)
    
print(client)