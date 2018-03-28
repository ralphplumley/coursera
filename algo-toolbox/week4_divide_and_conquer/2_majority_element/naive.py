# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    
    for i in range(len(a)):
        currentElement = a[i]
        count = 0

        for j in range(len(a)):
            if a[j] == currentElement:
                count += 1

    half = len(a) / 2
    if count > half:
        print('currentElement: ', currentElement)
        return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) == 1:
        print(1)
    elif get_majority_element(a, 0, n) == 0:
        print(0)
    else:
        print('error')
