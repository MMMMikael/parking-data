import requests
from bs4 import BeautifulSoup
import statistics
import json

cities = {
    "Annecy": "annecy",
    "Annemasse": "annemasse",
    "Cluses": "cluses",
    "Thonon": "thonon",
    "Sallanches": "sallanches"
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

data = {"villes":[]}

for city, query in cities.items():

    url = f"https://www.leboncoin.fr/recherche?text=garage&locations={query}"

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    prices = []

    for span in soup.find_all("span"):

        text = span.get_text()

        if "€" in text:

            text = text.replace("€","").replace(" ","")

            try:
                price = int(text)

                if price < 100000:
                    prices.append(price)

            except:
                pass

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

with open("data.json","w") as f:

    json.dump(data,f,indent=2)

print("data updated")
