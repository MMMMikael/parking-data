import requests
from bs4 import BeautifulSoup
import statistics
import json

cities = {
    "Annecy": "annecy-74",
    "Annemasse": "annemasse-74",
    "Cluses": "cluses-74",
    "Thonon": "thonon-les-bains-74",
    "Sallanches": "sallanches-74"
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

data = {"villes":[]}

for city, slug in cities.items():

    url = f"https://www.seloger.com/list.htm?types=2&projects=2&places=[{{ci:{slug}}}]&enterprise=0&qsVersion=1.0&types=2&natures=1&categories=garage"

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    prices = []

    for span in soup.find_all("span"):

        text = span.get_text()

        if "€" in text:

            text = text.replace("€","").replace(" ","")

            try:

                price = int(text)

                if 2000 < price < 100000:

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
