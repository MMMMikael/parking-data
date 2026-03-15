import requests
import json
import statistics

cities = {
    "Annecy": "annecy",
    "Annemasse": "annemasse",
    "Cluses": "cluses",
    "Thonon": "thonon",
    "Sallanches": "sallanches"
}

data = {"villes":[]}

url = "https://api.leboncoin.fr/finder/search"

headers = {
    "Content-Type": "application/json"
}

for city, location in cities.items():

    payload = {
        "text": "garage",
        "location": location,
        "limit": 50
    }

    try:

        r = requests.post(url, headers=headers, json=payload)

        result = r.json()

        prices = []

        for ad in result.get("ads", []):

            if "price" in ad and ad["price"]:

                price = ad["price"][0]

                if price < 100000:

                    prices.append(price)

        if prices:

            avg_price = int(statistics.mean(prices))

            rendement = round((80*12)/avg_price*100,1)

        else:

            avg_price = 0
            rendement = 0

        data["villes"].append({
            "ville": city,
            "prix": avg_price,
            "rendement": rendement,
            "annonces": len(prices)
        })

    except:

        data["villes"].append({
            "ville": city,
            "prix": 0,
            "rendement": 0,
            "annonces": 0
        })

with open("data.json","w") as f:

    json.dump(data,f,indent=2)

print("data updated")
