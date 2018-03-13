# Uses python3
import sys

def gcd_euclid(a, b):
  if (b == 0):
    return a
  
  aPrime = a % b
  return gcd_euclid(b, aPrime)

def lcm(a, b):
    return int( (a // gcd_euclid(a, b)) * b)

if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print(lcm(a, b))