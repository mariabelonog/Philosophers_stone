    import csv

    with open('just_words.csv', encoding="utf8") as csvfile1, open('words2.csv', 'w', newline='') as csvfile:
        reader = csv.reader(csvfile1, delimiter='-', quotechar='"')
        writer = csv.writer(
            csvfile, delimiter='+', quotechar='"', )

    for index, row in enumerate(reader):
        st = row
        new_line = list()
        for i in st:
            new_word = ''
            for j in i:
                if j in 'qwertyuioplkjhgfdsazxcvbnmйцукенгшщзхъёэждлорпавыфячсмитьбю':
                    new_word += j
            new_line.append(new_word)
        new_line1 = []
        for i in new_line:
            if i:
                new_line1.append(i)
        new_line = '/'.join(new_line1)
        writer.writerow([new_line])