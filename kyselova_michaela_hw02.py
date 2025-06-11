import csv
import json

with open("netflix_titles.tsv", mode="r", encoding="utf-8") as file:
    data = list(csv.DictReader(file, delimiter="\t"))
    
output = []

for row in data:
    movie = {}

    movie["title"] = row["PRIMARYTITLE"].strip()

    director = row["DIRECTOR"].strip()
    movie["directors"] = [d.strip() for d in director.split(",")] if director else []

    cast = row["CAST"].strip()
    movie["cast"] = [c.strip() for c in cast.split(",")] if cast else []

    genres = row["GENRES"].strip()
    movie["genres"] = [g.strip() for g in genres.split(",")]

    year = row["STARTYEAR"].strip()
    if year.isdigit():
        movie["decade"] = int(year) - int(year) % 10
        output.append(movie)
        
with open("netflix_titles.json", mode="w", encoding="utf-8") as json_file:
    json.dump(output, json_file, ensure_ascii=False, indent=4)
