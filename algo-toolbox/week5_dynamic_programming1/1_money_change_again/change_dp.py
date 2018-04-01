# Uses python3
import sys
import math

def get_change(m):
    # denominations are 1, 3, 4

    # m = 6
    # [ inf inf inf inf inf inf ]
    # [ -1  -1  -1  -1  -1  -1  ]

    coins = [1,3,4]
    numCoins = [0]
    denomUsed = [] # the number inserted indicates coins[#], so 1, 3, or 4

    for i in range(m+1):
        numCoins.append(math.inf)
        denomUsed.append(-1)
    
    numCoins = numCoins[:-1]

    for j in range(len(coins)): # go through each coin
        for i in range(1, m+1):
            if i >= coins[j]:
                if (numCoins[i - coins[j]] + 1) < numCoins[i]:
                    numCoins[i] = 1 + numCoins[i - coins[j]]
                    denomUsed[i] = j;
        
    return numCoins[-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
