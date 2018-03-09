# Uses python3
def calc_fib_2(n):
  if (n <= 1):
    return n
    
  arr = [0,1]

  for i in range(2, n):
    arr.insert(i, ((arr[i-1] + arr[i-2]) % 10))

  arrLength = len(arr)
  fibNumber = (arr[arrLength-1] + arr[arrLength-2])

  if (fibNumber >= 10):
    return fibNumber % 10

  return fibNumber

n = int(input())
print(calc_fib_2(n))

# T(n) = 2n + 2
# So T(100) = 202