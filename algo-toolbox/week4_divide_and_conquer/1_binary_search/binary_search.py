# Uses python3
import sys

# 3 1 5 8
# 8 1 23

def binary_search(a, target):
    print('')
    left, right = 0, len(a)
    # write your code here
    print('a: ', a)
    print('target: ', target)
    print('left index: ', left)
    print('right index: ', right)

def linear_search(a, target):
    for i in range(len(a)):
        if a[i] == target:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read() # for Coursera submission

    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, target), end = ' ')
