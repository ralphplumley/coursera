from random import randint

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_2(n):
  arr = [0,1]

  for i in range(2, n):
    arrLength = len(arr)
    toAppend = arr[arrLength-1] + arr[arrLength-2]
    arr.append(toAppend)

  return arr[n-1] + arr[n-2]

while (True):
  random_n = randint(3, 25)
  print('random number: ', random_n)

  res1 = calc_fib(random_n)
  res2 = calc_fib_2(random_n)

  if res1 != res2:
    print('Wrong answer: ', res1, ' | ', res2)
    break
  else:
    print('OK')

