import csv
import pymorphy2
from filters import filter_city_adj


with open('words2.csv', encoding="utf8") as csvfile1,  open('noun-adj.csv', 'w', newline='') as csvfile:
    reader = csv.reader(csvfile1, delimiter='/', quotechar='"')
    writer = csv.writer(
        csvfile, delimiter='|', quotechar='"', )

    d1 = {}
    morph = pymorphy2.MorphAnalyzer()

    for index, row in enumerate(reader):
        if index == 0:
            continue
        for i in range(len(row)):
            if morph.parse(row[i])[0].tag.POS == 'NOUN':
                if i > 0:
                    if morph.parse(row[i - 1])[0].tag.POS in {'PRTF', "ADJF"}:
                        if row[i] in d1.keys():
                            d1[row[i]].append(row[i-1])
                        else:
                            d1[row[i]] = [row[i-1]]
                if i + 1 < len(row):
                    if morph.parse(row[i + 1])[0].tag.POS in {'NOUN', 'PRTF'}:
                        if row[i] in d1.keys():
                            d1[row[i]].append(row[i + 1])
                        else:
                            d1[row[i]] = [row[i + 1]]
    for i in d1.keys():
        s = list(set(d1[i]))
        s1 = d1[i].copy()
        s1 = filter_city_adj(s1)
        s.sort(key=lambda x: s1.count(x))
        print(i, s)
        writer.writerow([i, s])
"""
получение базы данных для прилагательных, которые чаще всего встречаются с каждым из существительных
"""