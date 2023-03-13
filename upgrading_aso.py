def aso_upgrade(aso):
    from search_functions import adj_search, search_frequency, noun_search, verb_search
    from syn_parcing import syn_parcing
    import pymorphy2
    morph = pymorphy2.MorphAnalyzer()
    pos = morph.parse(aso)[0].tag.POS
    body = []
    char_syn = syn_parcing(aso)
    if pos == 'ADJF' or pos == 'PRTF':
        for i in char_syn:
            if adj_search(i):
                body.append(i)
        if not body:
            if adj_search(aso):
                body.append(adj_search(aso)[0])
        return body
    elif pos == 'NOUN':
        for i in char_syn:
            if noun_search(i):
                body.append(i)
        if not body:
            if noun_search(aso):
                body.append(noun_search(aso)[0])
    elif pos == 'VERB' or pos == 'INFN':
        for i in char_syn:
            if verb_search(i):
                body.append(i)
        if not body:
            if verb_search(aso):
                body.append(verb_search(aso)[0])
    return body
print(aso_upgrade('работать'))