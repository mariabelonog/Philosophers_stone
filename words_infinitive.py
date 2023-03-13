import pymorphy2
import csv


with open('results.csv', encoding="utf8") as csvfile1, open('infinitives.csv', 'w', newline='') as csvfile:
    reader = csv.reader(csvfile1, delimiter='-', quotechar='"')
    writer = csv.writer(
        csvfile, delimiter='-', quotechar='"',
        quoting=csv.QUOTE_MINIMAL)
    morph = pymorphy2.MorphAnalyzer()
    for index, row in enumerate(reader):
        if index == 1:
            continue
        s = row[0].split('/')
        new_line = []
        for i in s:
            new_line.append(morph.parse(i)[0].normal_form)
        writer.writerow([' | '.join(new_line), row[1]])