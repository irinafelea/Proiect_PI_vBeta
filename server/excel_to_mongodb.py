import pandas as pd
from pymongo import MongoClient
import json

import excel_processing

client = MongoClient("mongodb://localhost:27017")
db = client["proiect"]
coll = db["ong"]

coll.delete_many({})

df = pd.read_excel("C:/Users/Irina/Desktop/PI/my-app/server/ong.xlsx", index_col=None)

json_file = json.loads(df.T.to_json()).values()

coll.insert_many(json_file)

email = "irina.felea02@e-uvt.ro"
coll.update_many({}, {'$push': {'e-mail': email}})

lista = []
coll.update_many({}, {'$push': {'lista de nevoi': lista}})
