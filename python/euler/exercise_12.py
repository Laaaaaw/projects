#What is the value of the first triangle number to have over five hundred divisors?
 
import math

def divisors(number):
    num_divisor = 0
    sqrt = int(math.sqrt(number))
 
    for i in range(1, sqrt, 1):
        if(number % i == 0):
            num_divisor += 2
        
    
 
    if (sqrt * sqrt == number):
        num_divisor -= 1
    
    return num_divisor

num = 0

p = 1 
while(divisors(num) < 500):
    num += p
    p += 1

print(num)
