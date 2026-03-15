import json
import random

cities = [
    "Annecy",
    "Annemasse",
    "Cluses",
    "Thonon",
    "Sallanches"
]

data = {"villes":[]}

for city in cities:

    price = random.randint(10000,20000)

    rendement = round((80*12)/price*100,1)

    data["villes"].append({
        "ville":city,
        "prix":price,
        "rendement":rendement
    })

with open("data.json","w") as f:
    json.dump(data,f,indent=2)

print("data updated")
