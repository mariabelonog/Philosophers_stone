def filter_city_adj(arr):
    from city_names import city_names
    nr = []
    for i in arr:
        for j in city_names:
            if j not in i:
                nr.append(i)
    return nr