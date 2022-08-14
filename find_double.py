# Есть массив из N чисел, каждое 0 <= m[i] <= N, все числа в массиве
# уникальны, только одно повторяется дважды. найдите дублирующееся число за
# линейное время и константное количество доп памяти"

from collections import Counter


def find_double(nums: list[int]) -> int:
    nums = Counter(nums)
    for k, v in nums.items():
        if v > 1:
            return k


assert find_double([0, 1, 2, 3, 4, 5, 6, 7, 7]) == 7
assert find_double([0, 0]) == 0
assert find_double([1, 0, 0]) == 0
assert find_double([2, 1, 4, 3, 1]) == 1
assert find_double([2, 4, 4, 3, 1]) == 4
