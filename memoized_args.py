def memoized(function):
    memory = {}

    def inner(*numbers):
        memoized_result = memory.get(*numbers)
        if memoized_result is None:
            memoized_result = function(numbers)
            memory[numbers] = memoized_result
        return memoized_result
    return inner


@memoized
def f(*args: int) -> int:
    print('Calculating...')
    return args * 10


print(f((1, 2, 3, 4)))
