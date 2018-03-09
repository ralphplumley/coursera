# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
index1 = 1

a = sorted(a)
lastIndex = len(a) - 1
secondToLastIndex = len(a) - 2
output = a[lastIndex] * a[secondToLastIndex]
print(output)