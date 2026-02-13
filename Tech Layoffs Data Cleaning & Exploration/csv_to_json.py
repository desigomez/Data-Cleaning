import csv, json

with open('layoffs.csv', newline='') as f:
    reader = csv.DictReader(f)
    data = list(reader)

with open('layoffs.json', 'w') as f:
    json.dump(data, f, indent=2)