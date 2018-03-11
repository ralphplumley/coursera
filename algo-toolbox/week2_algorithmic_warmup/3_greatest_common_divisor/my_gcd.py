# Uses python3

# def gcd_naive(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d

#     return current_gcd

# print(gcd_naive(100, 25))

def gcd_euclid(a, b):
  if (b == 0):
    return a
  
  aPrime = a % b
  return gcd_euclid(b, aPrime)

print(gcd_euclid(10, 5))
  