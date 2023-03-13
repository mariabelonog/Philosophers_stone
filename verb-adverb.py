import csv
import pymorphy2


with open('words2.csv', encoding="utf8") as csvfile1,  open('verb-adverb.csv', 'w', newline='') as csvfile:
    reader = csv.reader(csvfile1, delimiter='/', quotechar='"')
    writer = csv.writer(
        csvfile, delimiter='|', quotechar='"', )

    d = {}
    morph = pymorphy2.MorphAnalyzer()

    for index, row in enumerate(reader):
        if index == 0:
            continue
        for i in range(len(row)):
            if morph.parse(row[i])[0].tag.POS in {'VERB', 'INFN'}:
                if i > 0:
                    if morph.parse(row[i - 1])[0].tag.POS in {'ADVB', 'GRND', 'NOUN'}:
                        if row[i] in d.keys():
                            d[row[i]].append(row[i - 1])
                        else:
                            d[row[i]] = [row[i-1]]
                if i + 1 < len(row):
                    if morph.parse(row[i + 1])[0].tag.POS in {'ADVB', 'GRND', 'NOUN'}:
                        if row[i] in d.keys():
                            d[row[i]].append(row[i + 1])
                        else:
                            d[row[i]] = [row[i+1]]
    for i in d.keys():
        s = list(set(d[i]))
        s1 = d[i].copy()
        s.sort(key=lambda x: s1.count(x))
        print(i, s)
        writer.writerow([i, s])

"""
получение базы данных для наречий и деепричастий, которые чаще всего встречаются с каждым из глаголов
"""