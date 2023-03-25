import csv

with open('results.csv', encoding="utf8") as csvfile1, open('results3.csv', 'w', newline='') as csvfile:
    reader = csv.reader(csvfile1, delimiter='-', quotechar='"')
    writer = csv.writer(
        csvfile, delimiter='-', quotechar='"',
        quoting=csv.QUOTE_MINIMAL)
    for index, row in enumerate(reader):
        if index != 1 and index !=0:
            writer.writerow([row[0]])