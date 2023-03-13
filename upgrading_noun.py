def noun_upgrade(noun, char, sim):
    from search_functions import noun_search, search_frequency
    from syn_parcing import syn_parcing
    import pymorphy2


    morph = pymorphy2.MorphAnalyzer()
    syns_char = syn_parcing(char)
    syns_sim = syn_parcing(sim)
    body = []
    s = noun_search(noun)
    print(s)
    if s:
        for i in s:
            if i in syns_char or i == char:
                body.append(i)
            if i in syns_sim or i == sim and i not in body:
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
                body2.append(new_body[i])
                body = body2
        else:
            body.append(s[0])
    return body
print(noun_upgrade('организация', 'волонтеры', 'беженцы'))