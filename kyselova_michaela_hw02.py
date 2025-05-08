import csv
import json

with open("netflix_titles.tsv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter="\t")
    data = list(reader)

new_data = []
wanted_keys = ["PRIMARYTITLE", "DIRECTOR", "CAST", "GENRES", "STARTYEAR"]

for row in data:
    new_row = {}
    for key in wanted_keys:
        if key in row:
            new_row[key] = row[key]
    new_data.append(new_row)

rename = {
    "PRIMARYTITLE": "title",
    "DIRECTOR": "directors",
    "CAST": "cast",
    "GENRES": "genres",
    "STARTYEAR": "decade"
}

for row in new_data:
    for old_key, new_key in rename.items():
        if old_key in row:
            row[new_key] = row.pop(old_key)
    
    for key, delimiter in [
            ("directors", ", "), ("cast", ", "), ("genres", ",")]:
        value = row.get(key)
        if value:
            row[key] = value.split(delimiter)
        else:
            row[key] = []
    
    year = int(row["decade"])
    row["decade"] = year - (year % 10)

with open("netflix_titles.json", mode="w", encoding="utf-8") as json_file:
    json.dump(new_data, json_file, ensure_ascii=False, indent=4)
