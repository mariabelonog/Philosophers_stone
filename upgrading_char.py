def char_upgrade(char):
    from search_functions import adj_search, search_frequency, noun_search
    from syn_parcing import syn_parcing
    import pymorphy2
    morph = pymorphy2.MorphAnalyzer()
    pos = morph.parse(char)[0].tag.POS
    body = []
    char_syn = syn_parcing(char)
    if pos == 'ADJF' or pos == 'PRTF':
        for i in char_syn:
            if adj_search(i):
                body.append(i)
        if not body:
            if adj_search(char):
                body.append(adj_search(char)[0])
        return body
    elif pos == 'NOUN':
        for i in char_syn:
            if noun_search(i):
                body.append(i)
        if not body:
            if noun_search(char):
                body.append(noun_search(char)[0])
    return body

print(char_upgrade('детский'))