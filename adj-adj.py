import csv
import pymorphy2


with open('words2.csv', encoding="utf8") as csvfile1,  open('adj-adj.csv', 'w', newline='') as csvfile:
    reader = csv.reader(csvfile1, delimiter='/', quotechar='"')
    writer = csv.writer(
        csvfile, delimiter='|', quotechar='"', )
