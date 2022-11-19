#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.


#Function to check if a number is multiple of 3 or 5

def multiples(n):
    if(n%3 == 0 or n%5 == 0):
        return True
    else:
        return False

sum = 0

for i in range(1000):
  if multiples(i):
    sum += i


print(sum)
    