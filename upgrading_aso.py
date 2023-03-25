def aso_upgrade(noun, char, aso, syns_noun, syns_char, syns_sim):
    from search_functions import adj_search, search_frequency, noun_search, verb_search
    from syn_parcing import syn_parcing
    import pymorphy2
    from upgrading_noun import noun_upgrade

    morph = pymorphy2.MorphAnalyzer()
    pos = morph.parse(aso)[0].tag.POS
    body = []

    for i in syns_sim:
        if search_frequency(i) > search_frequency(aso):
            aso = i
    if pos == 'ADJF' or pos == 'PRTF':
        for i in syns_sim:
            if adj_search(i):
                body.extend(i)
        if not body:
            if adj_search(aso):
                body.extend(adj_search(aso)[0])
        return body
    elif pos == 'NOUN':
        body = noun_upgrade(aso, char, aso, syns_sim, syns_char, syns_sim)
    elif pos == 'VERB' or pos == 'INFN':
        for i in syns_sim:
            s = set(verb_search(i))
            s1 = set(syns_noun)
            if s:
                if s.intersection(s1):
                    body.extend(list(s.intersection(s1)))
        if not body:
            if verb_search(aso):
                body.extend(verb_search(aso)[0])
    return body
