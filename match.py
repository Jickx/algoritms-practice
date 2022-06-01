def find_match(l):
    """ [1, 1, 2, 3, 1, 3] -> [1, 3] """
    seen, match = set(), []
    for i in l:
        if i in seen and i not in match:
            match.append(i)
        else:
            seen.add(i)
    return match

assert find_match([1, 1, 2, 3, 1, 3]) == [1, 3]
assert find_match([0, 1, 3]) == []
assert find_match([]) == []
assert find_match([1, 1, 1, 1, 1]) == [1]
assert find_match([1, 3, 1, 3, 1, 3]) == [1,3]
assert find_match([-1, -1, -1, 0, 0, 0]) == [-1,0]
