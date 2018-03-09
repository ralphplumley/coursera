# Uses python3
def calc_fib(x):
    if (n < 0):
        return 'no negative numbers please'

    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
print(calc_fib(n))
