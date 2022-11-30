#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

limit = 101
sum = 0
sum2 = 0

for i in range(limit):
    sum += i*i


for j in range(limit):
    sum2 += j

solution = (sum2*sum2)-sum


print(solution)