import pymorphy2
import csv

with open('words2.csv', encoding="utf8") as csvfile1,  open('adj_freq.csv', 'w', newline='') as csvfile,\
        open('words2.csv', encoding="utf8") as csvfile2:
    reader = csv.reader(csvfile1, delimiter='/', quotechar='"')
    writer = csv.writer(
        csvfile, delimiter='|', quotechar='"', )
    writer.writerow('Частота прилагательных')
    s = []
    d = {}
    morph = pymorphy2.MorphAnalyzer()

    for index, row in enumerate(reader):
        if index == 0:
            continue

        for j in row:
            if morph.parse(j)[0].tag.POS in {'ADJF', 'PRTF'}:
                s.append(j)

    s_set = list(set(s))
    for i in s_set:
        d[i] = s.count(i)

    dic = {}
    reader2 = csv.reader(csvfile2, delimiter='/', quotechar='"')
    for index, row in enumerate(reader2):
        if index == 0:
            continue
        for i in range(len(row)):
            if morph.parse(row[i])[0].tag.POS in {'ADJF', 'PRTF'}:
                if i > 0:
                    if morph.parse(row[i - 1])[0].tag.POS in {'ADJF', 'PRTF'}:
                        if row[i - 1] in dic.keys():
                            dic[row[i-1]].append(row[i])
                        else:
                            dic[row[i - 1]] = []
            elif morph.parse(row[i])[0].tag.POS in {'ADJF', 'PRTF'}:
                if i + 1 < len(row):
                    if morph.parse(row[i + 1])[0].tag.POS in {'ADJF', 'PRTF'}:
                        if row[i] in dic.keys():
                            dic[row[i]].append(row[i + 1])
                        else:
                            dic[row[i]] = []

    for i in dic.keys():
        dic[i] = list(set(dic[i]))
        dic[i].sort(key=lambda x: -d[x])
        writer.writerow([i, dic[i]])

"""
Формирование базы данных с прилагательными и самыми частыми словами, котороые с ними употребляются
"""