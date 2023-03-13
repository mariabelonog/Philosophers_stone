import pymorphy2
import csv


d = {}
with open('words2.csv', encoding="utf8") as csvfile1:
    reader = csv.reader(csvfile1, delimiter='-', quotechar='"')

    morph = pymorphy2.MorphAnalyzer()
    for index, row in enumerate(reader):
        if index == 0:
            continue
        s = row[0].split('/')
        new_line = list()
        for i in s:
            new_line.append(str(morph.parse(i)[0].tag.POS))
        new_line = "-".join(new_line)
        if new_line in d.keys:
            d[new_line] += 1
        else:
            d[new_line] = 1


d_s = d.items()
d_s.sort(lambda x: x[1])
print(d_s)