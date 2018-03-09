# Uses python3
def calc_fib_2(n):
  if (n <= 1):
    return n
    
  arr = [0,1]

  for i in range(2, n):
    # print()
    # print(i)
    # print('arr: ', arr)
    # arrLength = len(arr)
    # toAppend = arr[arrLength-1] + arr[arrLength-2]
    # arr.append(toAppend)
    # arr.insert(i, (arr[i-1] + arr[i-2]))
    arr.insert(i, (arr[i-1] + arr[i-2]) % 10)
    

  # print(arr)
  return arr[n-1]

n = int(input())
print(calc_fib_2(n))

# T(n) = 2n + 2
# So T(100) = 202