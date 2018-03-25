# Uses python3
import sys
import math

# 8 1 3 5 5 7 9 11 13
# 1 9

def binary_search(arr, target):
    minIndex, maxIndex = 0, len(arr) - 1

    while maxIndex >= minIndex:
        midIndex = math.floor((minIndex + maxIndex) / 2)

        if arr[midIndex] == target:
            return midIndex
        elif arr[midIndex] < target:
            minIndex = midIndex + 1
        else:
            maxIndex = midIndex - 1

    return -1
    

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
    arr = data[1 : n + 1]
    for target in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(arr, target), end = ' ')
