def set_as_done():
    dev_free, x, y = max_dev_free()
    couple_points = find_couples()
    number_of_matches, ids, couple_points = find_n_best_matches(dev_free, couple_points, dev_pandas_sorted)
    map_int[x][y] = 0
    for id in ids:
        if map_int[x + 1][y] != 0:
            map_int[x + 1][y] = 0
            dev_pandas.iloc[id].x = x + 1
            dev_pandas.iloc[id].y = y
        elif map_int[x][y + 1] != 0:
            map_int[x][y + 1] = 0
            dev_pandas.iloc[id].x = x
            dev_pandas.iloc[id].y = y + 1
        elif map_int[x - 1][y] != 0:
            map_int[x - 1][y] = 0
            dev_pandas.iloc[id].x = x - 1
            dev_pandas.iloc[id].y = y
        elif map_int[x][y - 1] != 0:
            map_int[x][y - 1] = 0
            dev_pandas.iloc[id].x = x
            dev_pandas.iloc[id].y = y - 1
    return number_of_matches