# Uses python3
import sys

def get_change(m):
    #write your code here
    output = (m // 10) + ( (m % 10) // 5 + (m % 5) )
    # print('Dimes: ', m//10)
    # print('Nickels', (m%10)//5)
    # print('Pennies', m%5)
    return output

if __name__ == '__main__':
    # m = int(sys.stdin.read())
    input = int(input())
    print(get_change(input))
