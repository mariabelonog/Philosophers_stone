import csv

with open('new_csv.csv', encoding="utf8") as csvfile1,open('words2.csv', encoding="utf8") as csvfile2, open(
        'results1.csv', 'w', newline='') as csvfile:
    reader = csv.reader(csvfile1, delimiter='-', quotechar='"')
    writer = csv.writer(
        csvfile, delimiter='-', quotechar='"',
        quoting=csv.QUOTE_MINIMAL)
    st = []
    for index, row in enumerate(reader):
        s = row[0]
        new_line = ''
        for i in s:
            if i != '"' and i != "'":
                new_line += i
        st.append(new_line)
    reader = csv.reader(csvfile2, delimiter='-', quotechar='"')
    for index, row in enumerate(reader):
        line = []
        line.append(row)
        line.append(st[index - 1])
        writer.writerow(line)