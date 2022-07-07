# Write a function: def solution(N) that, given an integer N, returns the
# smallest integer greater than N, the sum of whose digits is twice as big
# as the sum of digits of N.
# Examples:
# 1. Given N = 14, the function should return 19. The sum of digits of 19
# (1 + 9 = 10) is twice as big as sum of digits of 14 (1 + 4 = 5).
# 2. Given N = 10, the function should return 11.
# 3. Given N = 99, the function should return 9999.
# N is an integer within the range [1..500].


def solution(n):
    n_sum = sum(int(i) for i in str(n))
    result = n
    while True:
        result += 1
        result_sum = sum(int(i) for i in str(result))
        if result_sum == n_sum * 2:
            return result


assert solution(1) == 2
assert solution(14) == 19
assert solution(10) == 11
assert solution(99) == 9999
assert solution(500) == 505
