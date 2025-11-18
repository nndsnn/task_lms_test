import csv

substring = input().strip().lower()

with open('past.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = []
    for row in reader:
        if substring in row['character'].lower():
            data.append((int(row['year']), row['name']))

data.sort(key=lambda x: (x[0], x[1]))

result = [name for year, name in data]
print(' '.join(result))
