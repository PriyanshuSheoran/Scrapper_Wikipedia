import requests
from bs4 import BeautifulSoup
import csv


print("List Of Actors: https://en.wikipedia.org/wiki/Lists_of_actors")

actor_data = []

chinese_url = "https://en.wikipedia.org/wiki/List_of_Chinese_actors"
response = requests.get(chinese_url)
soup = BeautifulSoup(response.text, "html.parser")

print("1. Chinese Actors:", chinese_url)

content_div = soup.find("div", class_="mw-parser-output")
chinese_actors = content_div.select("ul li a[href^='/wiki/']")[:5]


for actor in chinese_actors:
    actor_name = actor.text.strip()
    actor_link = "https://en.wikipedia.org" + actor["href"]

    r = requests.get(actor_link)
    s = BeautifulSoup(r.text, "html.parser")

    born = occupation = education = "Not available"

    infobox = s.find("table", class_="infobox")
    if infobox:
        rows = infobox.find_all("tr")
        for row in rows:
            header = row.find("th")
            data = row.find("td")
            if header and data:
                label = header.text.strip().lower()
                if "born" in label and born == "Not available":
                    born = " ".join(data.stripped_strings)
                elif "occupation" in label and occupation == "Not available":
                    occupation = ", ".join(data.stripped_strings)
                elif "education" in label and education == "Not available":
                    education = ", ".join(data.stripped_strings)

    print(f"Actor: {actor_name}")
    print(f"Born: {born}")
    print(f"Occupation: {occupation}")
    print(f"Education: {education}")
    print("-" * 40)

    actor_data.append({
        "Country": "China",
        "Name": actor_name,
        "Born": born,
        "Occupation": occupation,
        "Education": education
    })


indian_url = "https://en.wikipedia.org/wiki/List_of_Indian_male_film_actors"
response = requests.get(indian_url)
soup = BeautifulSoup(response.text, "html.parser")

print("2. Indian Male Film Actors:", indian_url)

indian_actors = soup.select("div.div-col li a[href^='/wiki/']")[:5]

for actor in indian_actors:
    actor_name = actor.text.strip()
    actor_link = "https://en.wikipedia.org" + actor["href"]

    r = requests.get(actor_link)
    s = BeautifulSoup(r.text, "html.parser")

    born = occupation = education = "Not available"

    infobox = s.find("table", class_="infobox")
    if infobox:
        rows = infobox.find_all("tr")
        for row in rows:
            header = row.find("th")
            data = row.find("td")
            if header and data:
                label = header.text.strip().lower()
                if "born" in label and born == "Not available":
                    born = " ".join(data.stripped_strings)
                elif "occupation" in label and occupation == "Not available":
                    occupation = ", ".join(data.stripped_strings)
                elif "education" in label and education == "Not available":
                    education = ", ".join(data.stripped_strings)

    print(f"Actor: {actor_name}")
    print(f"Born: {born}")
    print(f"Occupation: {occupation}")
    print(f"Education: {education}")
    print("-" * 40)

    actor_data.append({
        "Country": "India",
        "Name": actor_name,
        "Born": born,
        "Occupation": occupation,
        "Education": education
    })

with open("actors_data.csv", "w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["Country", "Name", "Born", "Occupation", "Education"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for actor in actor_data:
        writer.writerow(actor)


