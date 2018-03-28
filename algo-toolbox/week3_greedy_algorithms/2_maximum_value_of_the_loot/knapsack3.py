# Uses python3
import sys

# backpack = 9lbs max
# saffron $5000 | 4 lbs
# vanilla $200 | 3 lbs
# cinnamon $10 | 5 lbs

#input: 3 9 5000 4 200 3 10 5

def get_optimal_value(capacity, weights, values):
    
    totalValue = float(0)
    ratios = [float(value) / float(weight) for value, weight in zip(values, weights)]

    for i in range(len(weights)):
        if capacity == 0:
            return totalValue
            break

        max_weight = max(ratios)
        index = ratios.index(max_weight)

        ratios[index] = 0
        
        weightToAdd = min(capacity, weights[index])

        totalValue += weightToAdd * max_weight
        weights[index] -= weightToAdd
        capacity -= weightToAdd

    return totalValue


if __name__ == "__main__":
    # data = list(map(int, sys.stdin.read().split()))
    data = list(map(int, input().split()))
    print('data', data)

    n, capacity = data[0:2]
    print('n: ', n)
    print('capacity: ', capacity)
    print('data[0:3]: ', data[0:3])

    values = data[2:(2 * n + 2):2]
    print('values: ', values)
    
    weights = data[3:(2 * n + 2):2]
    print('weights: ', weights)
    
    opt_value = get_optimal_value(capacity, weights, values)
    print('opt_value: ', opt_value)
    
    print("{:.10f}".format(opt_value))
