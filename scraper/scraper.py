import requests
import json

url = "https://www.data.gouv.fr/api/1/datasets/r/6c0f1d0d-9a40-4c7f-bfe1-d8b9b16c0da6"

r = requests.get(url)

data = r.json()

prices = []

for row in data:

    if row["code_departement"] == "74":

        if "garage" in row["type_local"].lower():

            prices.append(row["valeur_fonciere"])

avg_price = sum(prices) / len(prices)

output = {
    "villes":[
        {
            "ville":"Haute-Savoie",
            "prix":int(avg_price),
            "rendement":round((80*12)/avg_price*100,1),
            "annonces":len(prices)
        }
    ]
}

with open("data.json","w") as f:

    json.dump(output,f,indent=2)
