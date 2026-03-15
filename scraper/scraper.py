import requests
import csv
import io
import json
import statistics

url = "https://files.data.gouv.fr/geo-dvf/latest/csv/2023/departements/74.csv.gz"

r = requests.get(url)

# lire le CSV
content = io.StringIO(r.text)

reader = csv.DictReader(content)

prices = []

for row in reader:

    try:

        if row["code_departement"] == "74":

            if row["type_local"] == "Dépendance":

                price = float(row["valeur_fonciere"])

                if price > 1000:

                    prices.append(price)

    except:
        pass

if prices:

    avg_price = int(statistics.mean(prices))

else:

    avg_price = 0

data = {
    "villes":[
        {
            "ville":"Haute-Savoie",
            "prix":avg_price,
            "rendement":round((80*12)/avg_price*100,1) if avg_price else 0,
            "annonces":len(prices)
        }
    ]
}

with open("data.json","w") as f:

    json.dump(data,f,indent=2)

print("data updated")
