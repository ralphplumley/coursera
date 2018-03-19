# Uses python3
import sys

# backpack = 9lbs max
# saffron $5000 | 4 lbs
# vanilla $200 | 3 lbs
# cinnamon $10 | 5 lbs

#input: 3 9 5000 4 200 3 10 5

def get_optimal_value(capacity, weights, values):
    # write your code here
    # print('capacity: ', capacity)
    # print('weights: ', weights)
    # print('values: ', values)

    # print(capacity // weights[0])
    # print((capacity % weights[0]) // weights[1])
    # print(capacity // weights[0])

    arr = []
    totalValue = 0
    cap = capacity

    n = len(weights)
    i = 0
    j = 0

    while i < n:
      if cap == 0:
        return totalValue

      bestItemValue = 0

      while j < n:
        currentValue = (values[j]/weights[j])

        # print('--------------')
        # print('values[j]', values[j])
        # print('weights[j]', weights[j])
        # print('currentValue', currentValue)

        if (weights[j] > 0):
          if ( currentValue > bestItemValue ):
            bestItemValue = currentValue

        a = min(weights[j], cap)

        j += 1


      print('bestItemValue: ', bestItemValue)
      i += 1
      
    return 11111111111111


def getBiggerValue(a, b):
  if (a >= b):
    return a

  if (b > a):
    return b

if __name__ == "__main__":
    # data = list(map(int, sys.stdin.read().split()))
    data = list(map(int, input().split()))
    
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

# While Knapsack is not full
  # Choose item i w/ maximum vi / wi

  # If item fits into knapsack, take all of it
  # Otherwise, take so much as to fill the knapsack

# Return total value and amounts taken