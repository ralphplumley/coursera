# Uses python3
import sys
from random import randint

def gcd_euclid(a, b):
  if (b == 0):
    return a
  
  aPrime = a % b
  return gcd_euclid(b, aPrime)

def lcm(a, b):
    gcd = gcd_euclid(a, b)
    # print('gcd: ', gcd)
    return int((a * b) / gcd)
    # return (a * b) / gcd

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

while (True):
  random_n_a = randint(100, 1000)
  random_n_b = randint(100, 1000)
  print('a: ', random_n_a)
  print('b: ', random_n_b)

  res1 = lcm(random_n_a, random_n_b)
  res2 = lcm_naive(random_n_a, random_n_a)

  if res1 != res2:
    print('Wrong answer: ', res1, ' | ', res2)
    break
  else:
    print('OK')


# if __name__ == '__main__':
#     input = input()
#     a, b = map(int, input.split())
#     print(lcm(a, b))

