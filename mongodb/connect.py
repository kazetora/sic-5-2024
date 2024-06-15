from pymongo.mongo_client import MongoClient

uri = "<mongoDB URI>"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection

db = client.iotdb

sampledata = {
    "temperature": 25,
    "humidity": 80
}

try:
    # db.temperatureHumidiy.insert_one(sampledata)
    for data in db.temperatureHumidiy.find():
        print(data)
    
except Exception as e:
    print(e)