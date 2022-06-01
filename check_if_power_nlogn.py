def check_if_power(int_list):
    squared_set = set(int_list)
    result = []
    for i in int_list:
        squared = pow(i, 2)
        if squared in squared_set:
            result.append(i)
            result.append(squared)
    # print(result)
    return result

assert check_if_power([5, 16, 4, 7, 25]) == [5, 25, 4, 16] # two matches
assert check_if_power([5, 11, 4, 7, 26]) == [] # no matches
assert check_if_power([]) == [] # empty list
assert check_if_power([-5, 10, 25, -100, 37]) == [-5, 25] # negative i and negative j
assert check_if_power([1]) == [1, 1] # number is power of two of itself
assert check_if_power([25, 5]) == [5, 25] # powered number is first in list