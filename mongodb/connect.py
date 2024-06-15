from pymongo.mongo_client import MongoClient
import time
import random

uri = "<mongoDB URI>"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection

db = client.iotdb

# /sensor1
sampledata = {
    "temperature": random.randint(20, 35),
    "humidity": random.randint(60, 90),
    "timestamp": time.now()
}

# /sensor1/temperature/all
"""
{
    "temperature": [
        {
            "value": 25,
            "timestamp": "2022-11-25 22:10:00"
        },
        {
            "value": 26,
            "timestamp": "2022-11-25 22:10:05"
        }
    ]
}
"""
# /sensor1/humidity/all
"""
{
    "humidity": [
        {
            "value": 80,
            "timestamp": "2022-11-25 22:10:00"
        },
        {
            "value": 85,
            "timestamp": "2022-11-25 22:10:05"
        }
    ]
}
"""

# /sensor1/temperature/avg
"""
{
    "temperature": {
        "avg": 25
    }
}
"""

# /sensor1/humidity/avg
"""
{
    "humidity": {
        "avg": 82.5
    }
}
"""

try:
    # db.temperatureHumidiy.insert_one(sampledata)
    for data in db.temperatureHumidiy.find():
        print(data)
    
except Exception as e:
    print(e)