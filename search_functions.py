def noun_search(noun):
    import csv
    with open('noun-adj.csv', encoding="utf8") as csvfile1:
        reader = csv.reader(csvfile1, delimiter='|', quotechar='"')
        for i, row in enumerate(reader):
            if row[0] == noun:
                return eval(row[1])
        return []


def search_frequency(word):
    import csv
    with open('word_freq.csv', encoding="utf8") as csvfile1:
        reader = csv.reader(csvfile1, delimiter='|', quotechar='"')
        for i, row in enumerate(reader):
            if row[0] == word:
                return int(row[1])
        return 0


def adj_search(adj):
    import csv
    with open('adj_freq.csv', encoding="utf8") as csvfile1:
        reader = csv.reader(csvfile1, delimiter='|', quotechar='"')
        for i, row in enumerate(reader):
            if row[0] == adj:
                return eval(row[1])
        return []


def verb_search(verb):
    import csv
    with open('verb-adverb.csv', encoding="utf8") as csvfile1:
        reader = csv.reader(csvfile1, delimiter='|', quotechar='"')
        for i, row in enumerate(reader):
            if row[0] == verb:
                return eval(row[1])
        return []
