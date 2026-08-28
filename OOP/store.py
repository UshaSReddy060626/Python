#creating json
import json
store={
    "name":"vmart",
    "city":"Bengaluru"
}
with open("store.json","w")as file:
    json.dump(store,file,indent=3)
print("store data saved")

#reading
import json
with open("store.json","r")as file:
    data=json.load(file)
print(data)
print("Name:",data["name"])
print("city:",data["city"])
