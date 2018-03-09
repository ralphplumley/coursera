from random import randint

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


while (True):
  random_n = randint(0, 9)
  
  res1 = calc_fib(random_n)
  res2 = calc_fib(random_n)

  if res1 != res2:
    print('Wrong answer: ', res1, ' | ', res2)
    break
  else:
    print('OK')

