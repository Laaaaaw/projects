#Find the sum of all the primes below two million.

def is_prime(n):
    if(n == 2):
        return True
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
# boolean array
    p = 2

    while (p * p <= num):

        if (prime[p] == True):
  
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1

    sum = 0

    for p in range(2, num+1):
        if prime[p]:
            sum += p
    return sum

limit = 2000000



print(SieveOfEratosthenes(limit))