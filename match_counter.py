from collections import Counter

def find_match(l):
    """ [1, 1, 2, 3, 1, 3] -> [1, 3] """
    counted = Counter(l)
    return [elem for elem, count in counted.items() if count > 1]

assert find_match([1, 1, 2, 3, 1, 3]) == [1, 3]
assert find_match([0, 1, 3]) == []
assert find_match([]) == []
assert find_match([1, 1, 1, 1, 1]) == [1]
assert find_match([1, 3, 1, 3, 1, 3]) == [1,3]
assert find_match([-1, -1, -1, 0, 0, 0]) == [-1,0]