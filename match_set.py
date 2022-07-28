def find_match(l):
    """ [1, 1, 2, 3, 1, 3] -> [1, 3] """
    match = set()
    result = []
    for elem in l:
        if elem not in match:
            match.add(elem)
        else:
            result.append(elem)
    print(result)
    return result


assert find_match([1, 1, 2, 3, 1, 3]) == [1, 3]
assert find_match([0, 1, 3]) == []
assert find_match([]) == []
assert find_match([1, 1, 1, 1, 1]) == [1]
assert find_match([1, 3, 1, 3, 1, 3]) == [1, 3]
assert find_match([-1, -1, -1, 0, 0, 0]) == [-1, 0]
