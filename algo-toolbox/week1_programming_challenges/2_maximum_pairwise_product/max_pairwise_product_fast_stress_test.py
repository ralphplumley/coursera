# Uses python3
def maxPairWiseFast():
  n = int(input())
  a = [int(x) for x in input().split()]
  assert(len(a) == n)

  result = 0
  index1 = 1

  for i in range(2, n):
    if a[i] > a[index1]:
      index1 = i

  if index1 == 1:
    index2 = 2
  else:
    index2 = 1
  for i in range(1, n):
    if a[i] != a[index1] and a[i] > a[index2]:
      index2 = i

  print(a[index1]*a[index2])

maxPairWiseFast()

def main():
  on = true
  while on = true:

main()