# Uses python3
import sys
import math

def get_majority_element(a, left, right):
  maj_index = 0
  count = 1

  for i in range(len(a)):
    if a[maj_index] == a[i]:
      count += 1
    else:
      count -= 1
    
    if count == 0:
      maj_index = i
      count = 1

  candidate = a[maj_index]
  # print('candidate: ', candidate)

  count = 0
  for i in range(len(a)):
    if a[i] == a[maj_index]:
      count += 1

  if count > right // 2:
    # return a[maj_index]
    return 1

  return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) == 1:
        print(1)
    elif get_majority_element(a, 0, n) == 0:
        print(0)
    else:
        print('error')
