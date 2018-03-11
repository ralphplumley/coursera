from random import randint

def gcd_euclid(a, b):
  if (b == 0):
    return a
  
  aPrime = a % b
  return gcd_euclid(b, aPrime)

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

while (True):
  random_n_a = randint(10000, 100000)
  random_n_b = randint(10000, 100000)
  print('a: ', random_n_a)
  print('b: ', random_n_b)

  res1 = gcd_euclid(random_n_a, random_n_b)
  res2 = gcd_naive(random_n_a, random_n_a)

  if res1 != res2:
    print('Wrong answer: ', res1, ' | ', res2)
    break
  else:
    print('OK')

