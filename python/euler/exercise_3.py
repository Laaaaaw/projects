#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

number = 600851475143
counter = 2
contador = number
solution = 0
while(counter^2 <= contador):
  if(contador % counter == 0):
    contador = contador / counter
    solution = counter
  else:
    counter += 1

  if(contador > solution):
    solution = contador

print(solution)
  