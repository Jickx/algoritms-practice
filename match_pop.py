def find_match(l):
    """ [1, 1, 2, 3, 1, 3] -> [1, 3] """
    match = []
    l.reverse()
    while l:
        elem = l.pop() 
        if elem in l and elem not in match:
            match.append(elem)
    print(match)
    return match

assert find_match([1, 1, 2, 3, 1, 3]) == [1, 3]
assert find_match([0, 1, 3]) == []
assert find_match([]) == []
assert find_match([1, 1, 1, 1, 1]) == [1]
assert find_match([1, 3, 1, 3, 1, 3]) == [1,3]
assert find_match([-1, -1, -1, 0, 0, 0]) == [-1,0]
