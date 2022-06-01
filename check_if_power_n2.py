def check_if_power(int_list):
    """ Check if numbers are power of two. """
    power_list = []
    for i in int_list:
        for j in int_list:
            if pow(i, 2) == j:
                power_list.append(i)
                power_list.append(j)
    # print(power_list)
    return power_list

assert check_if_power([5, 16, 4, 7, 25]) == [5, 25, 4, 16] # two matches
assert check_if_power([5, 11, 4, 7, 26]) == [] # no matches
assert check_if_power([]) == [] # empty list
assert check_if_power([-5, 10, 25, -100, 37]) == [-5, 25] # negative i and negative j
assert check_if_power([1, 0]) == [1, 1, 0, 0] # number is power of two of itself
assert check_if_power([25, 5]) == [5, 25] # powered number is first in list


