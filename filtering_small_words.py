import pymorphy2
import csv


with open('infinitives.csv', encoding="utf8") as csvfile1, open('just_words.csv', 'w', newline='') as csvfile:
    reader = csv.reader(csvfile1, delimiter='-', quotechar='"')
    writer = csv.writer(
        csvfile, delimiter='-', quotechar='"',
        quoting=csv.QUOTE_MINIMAL)
    morph = pymorphy2.MorphAnalyzer()
    writer.writerow(['WORDS'])
    for index, row in enumerate(reader):
        s = row[0].split(' | ')
        new_line = []
        for i in s:
            if 'PREP' not in morph.parse(i)[0].tag and 'CONJ' not in morph.parse(i)[0].tag \
                    and 'PRCL' not in morph.parse(i)[0].tag and 'INTJ' not in morph.parse(i)[0].tag \
                    and 'NPRO' not in morph.parse(i)[0].tag:
                new_line.append(i)
        writer.writerow(new_line)