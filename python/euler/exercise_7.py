#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

limit = 10001

contador = 0

number = 1

while(contador < limit):
    if(is_prime(number)):
        contador += 1
    if(contador != limit):
        number += 2

print(number)