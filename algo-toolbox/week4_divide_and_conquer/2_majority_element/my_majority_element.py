# Uses python3
import sys
import math

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    #write your code here

    if len(a) // 2 != 0:
        numForMajority = (math.ceil(len(a) / 2 )) + 1
    else:
        numForMajority = math.ceil(len(a) / 2 )

        
    count = {}

    for i in range(len(a)):
        currentElement = a[i]
        if currentElement in count:
            count[currentElement] += 1

            if count[currentElement] == numForMajority:
                return 1
        else:
            count[currentElement] = 1

    print('count: ', count)

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
