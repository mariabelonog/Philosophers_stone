import csv


d = {}
with open('words2.csv', encoding="utf8") as csvfile1,  open('word_freq.csv', 'w', newline='') as csvfile:
    reader = csv.reader(csvfile1, delimiter='/', quotechar='"')
    s = []
    dict_freq = {}

    for index, row in enumerate(reader):
        if index == 0:
            continue

        s.extend(row)

    s_set = list(set(s))
    new_list = []
    for i in s_set:
        new_list.append([i, s.count(i)])
    new_list.sort(key=lambda x: -x[1])

    writer = csv.writer(
        csvfile, delimiter='|', quotechar='"', )
    writer.writerow('Частота Слов')
    for i in new_list:
        dict_freq[i[0]] = i[1]
        writer.writerow(i)

""" 
наиболее часто встерчающиеся слова - для статистики + словарь для получения частотности
"""