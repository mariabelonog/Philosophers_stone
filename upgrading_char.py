def char_upgrade(noun, char, aso, syns_noun, syns_char, syns_sim):
    from search_functions import adj_search, search_frequency, noun_search
    from syn_parcing import syn_parcing
    import pymorphy2
    from upgrading_noun import noun_upgrade

    morph = pymorphy2.MorphAnalyzer()
    pos = morph.parse(char)[0].tag.POS
    body = []
    for i in syns_char:
        if search_frequency(i) > search_frequency(char):
            char = i
    if pos == 'ADJF' or pos == 'PRTF':
        s = adj_search(char)
        for i in syns_char:
            if i in s:
                body.append(i)
        if not body or len(body) == 1:
            if s:
                body.append(s[0])
                if len(s) > 1:
                    body.append(s[1])

        return body
    elif pos == 'NOUN':
        body = noun_upgrade(char, noun, aso, syns_char, syns_noun, syns_sim)
    return list(set(body))

