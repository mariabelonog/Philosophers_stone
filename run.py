def run(noun, char, aso):
    from syn_parcing import syn_parcing
    from upgrading_noun import noun_upgrade
    from upgrading_aso import aso_upgrade
    from upgrading_char import char_upgrade
    from search_functions import search_frequency

    syns_char = syn_parcing(char)
    syns_sim = syn_parcing(aso)
    syns_noun = syn_parcing(noun)


    a = noun_upgrade(noun, char, aso, syns_noun, syns_char, syns_sim)
    b = aso_upgrade(noun, char, aso, syns_noun, syns_char, syns_sim)
    c = char_upgrade(noun, char, aso, syns_noun, syns_char, syns_sim)


    for i in syns_sim:
        if search_frequency(i) > search_frequency(aso):
            aso = i

    for i in syns_char:
        if search_frequency(i) > search_frequency(char):
            char = i

    keywords = [noun, aso, char]

    keywords.extend(a)
    keywords.extend(b)
    keywords.extend(c)

    return list(set(keywords))
