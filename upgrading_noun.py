def noun_upgrade(noun, char, sim, syns_noun, syns_char, syns_sim):
    from search_functions import noun_search, search_frequency
    from syn_parcing import syn_parcing
    import pymorphy2


    morph = pymorphy2.MorphAnalyzer()
    body = []
    for i in syns_noun:
        if search_frequency(i) > search_frequency(noun):
            noun = i
    s = noun_search(noun)

    if s:
        for i in s:
            if i in syns_char or i == char:
                body.append(i)
            if i in syns_sim or i == sim:
                body.append(i)

        if body:
            new_body = {}
            body2 = []
            for i in body:
                pos = morph.parse(i)[0].tag.POS
                if pos in new_body.keys():
                    new_body[pos].append(i)
                else:
                    new_body[pos] = [i]
            for i in new_body.keys():
                new_body[i].sort(key=lambda x: -search_frequency(x))
                body2.extend(new_body[i])
            body = body2
        else:
            body.append(s[0])
            if len(s) > 1:
                body.append(s[1])
    return body
