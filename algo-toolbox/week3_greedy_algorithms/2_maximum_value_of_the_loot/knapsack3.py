# Uses python3
import sys

# backpack = 9lbs max
# saffron $5000 | 4 lbs
# vanilla $200 | 3 lbs
# cinnamon $10 | 5 lbs

#input: 3 9 5000 4 200 3 10 5

def get_optimal_value(capacity, weights, values):
    # write your code here
    print('capacity: ', capacity)
    print('weights: ', weights)
    print('values: ', values)

    # print(capacity // weights[0])
    # print((capacity % weights[0]) // weights[1])
    # print(capacity // weights[0])

    arr = []
    v = 0
    cap = capacity

    for element in weights:
        if capacity == 0:
            return arr[v]

    


if __name__ == "__main__":
    # data = list(map(int, sys.stdin.read().split()))
    data = list(map(int, input().split()))
    
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
