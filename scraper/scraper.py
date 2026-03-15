import requests
import gzip
import csv
import io
import json
import statistics
from collections import defaultdict

urls = [
"https://files.data.gouv.fr/geo-dvf/latest/csv/2023/departements/73.csv.gz",
"https://files.data.gouv.fr/geo-dvf/latest/csv/2023/departements/74.csv.gz"
]

cities = defaultdict(list)

for url in urls:

    r = requests.get(url)

    compressed = io.BytesIO(r.content)
    decompressed = gzip.GzipFile(fileobj=compressed)
    decoded = io.TextIOWrapper(decompressed, encoding="utf-8")

    reader = csv.DictReader(decoded)

    for row in reader:

        try:

            if row["type_local"] == "Dépendance":

                price = float(row["valeur_fonciere"])

                surface = row["surface_reelle_bati"]

                if surface == "" and 2000 < price < 60000:

                    city = row["nom_commune"]

                    cities[city].append(price)

        except:
            pass

results = []

for city, prices in cities.items():

    if len(prices) >= 5:

        avg_price = int(statistics.mean(prices))

        rendement = round((80*12)/avg_price*100,1)

        results.append({
            "ville": city,
            "prix": avg_price,
            "rendement": rendement,
            "annonces": len(prices)
        })

# prendre les 20 villes avec le plus d'annonces
results = sorted(results, key=lambda x: x["annonces"], reverse=True)[:20]

data = {"villes": results}

with open("data.json","w") as f:
    json.dump(data,f,indent=2)

print("data updated")
