import csv


with open('new_csv.csv', encoding="utf8") as csvfile1, open('projes.csv', 'w', newline='') as csvfile:
    reader = csv.reader(csvfile1, delimiter='-', quotechar='"')
    writer = csv.writer(
        csvfile, delimiter='-', quotechar='"',
        quoting=csv.QUOTE_MINIMAL)
    for index, row in enumerate(reader):
        writer.writerow([row[0]])