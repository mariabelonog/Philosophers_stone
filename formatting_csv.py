import csv

with open('results3.csv', encoding="utf8") as csvfile1, open('words2.csv', encoding="utf8") as csvfile2,\
        open('results4.csv', 'w', newline='') as csvfile:
    reader1 = csv.reader(csvfile1, delimiter='/', quotechar='"')
    reader2 = csv.reader(csvfile2, delimiter='/', quotechar='"')
    writer = csv.writer(
        csvfile, delimiter=',', quotechar='"',
        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['keywords', 'sentence'])
    s = []
    for index, row in enumerate(reader2):
        if index != 0 and index != 1:
            a = list(set(row))
            s.append(' '.join(a))
    for index, row in enumerate(reader1):
        b = ' '.join(row)
        writer.writerow([s[index], b])