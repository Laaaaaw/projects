def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def Largest_Prime_Factor(n):
    return next(n // i for i in range(1, n) if n % i == 0 and is_prime(n  // i))


print(Largest_Prime_Factor(600851475143))