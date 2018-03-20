# Uses python3
import sys
# from decimal import *
# getcontext().prec = 4

# backpack = 9lbs max
# saffron $5000 | 4 lbs
# vanilla $200 | 3 lbs
# cinnamon $10 | 5 lbs

#input: 3 9 5000 4 200 3 10 5

def get_optimal_value(capacity, weights, values):
    totalValue = 0
    cap = capacity

    n = len(weights)
    
    while (capacity > 0):
      bestValue = 0.000
      bestValueIndex = None

      for i in range(n):
        # print('-------------')
        # print('i: ', i)
        # print('value[i]: ', values[i])
        # print('weight[i]: ', weights[i])

        if (weights[i] > 0):
          currentValue = round(float(values[i]), 4) / round(float(weights[i]), 4)
          # print('currentValue: ', currentValue)

        if (weights[i] > 0 and (currentValue > bestValue)):
          bestValue = currentValue
          bestValueIndex = i

      # print('bestValue: ', bestValue)
      # print('bestValueIndex: ', bestValueIndex)
      # print('weights[bestValueIndex]: ', weights[bestValueIndex])

      if (int(weights[bestValueIndex]) <= int(capacity)):
        totalValue += (bestValue * weights[bestValueIndex])
        capacity = capacity - weights[bestValueIndex]
        weights[bestValueIndex] -= weights[bestValueIndex]
      else:
        amountToTake = capacity - weights[bestValueIndex]
        totalValue += (bestValue * (capacity - amountToTake))
        weights[bestValueIndex] - amountToTake
        capacity = capacity - amountToTake;

      # capacity = 0 # <-- make sure to delete

    return totalValue

if __name__ == "__main__":
    # data = list(map(int, sys.stdin.read().split()))
    data = list(map(int, input().split()))
    
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
