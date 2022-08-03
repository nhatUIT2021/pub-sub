import json
import requests



# Data to be written
dictionary ={
    "Name": "test",
    "DOB": "1/1/1990",
    "Sex": "Male",
  }
a= json.dumps(dictionary)
print (a[0].json)