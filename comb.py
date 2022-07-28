def comb(list1, list2):
    list3 = []
    for i in list1:
        for j in list2:
            list3.append((i, j))
    return list3


print(comb({1, 2, 3}, [4, 5]))
