#Find the sum of all the primes below two million.

def is_prime(n):
    if(n == 2):
        return True
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True


limit = 2000000

sum = 2

for i in range(2, limit):
    if(i%2 != 0):
        if(is_prime(i) == True):
            sum += i

print(sum)