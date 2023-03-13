import csv

with open('new_csv.csv', encoding="utf8") as csvfile1, open('results.csv', 'w', newline='') as csvfile:
    reader = csv.reader(csvfile1, delimiter='-', quotechar='"')
    writer = csv.writer(
        csvfile, delimiter='-', quotechar='"',
        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['rows'])
    for index, row in enumerate(reader):
        s = row[0].split()
        new_line = []
        for i in s:
            word = ''
            for j in i:
                if j.isalpha():
                    word += j
            new_line.append(word.lower())
        writer.writerow(['/'.join(new_line), row[1]])