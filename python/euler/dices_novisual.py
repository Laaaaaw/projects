import random

print("How many dices do you wanna throw?")
n = int(input())
print("How many times do you wanna throw")
times = int(input())

m = n*6-n+1
chances = [0] * m

def throw(n):
  result = 0
  for i in range(n):
    result += random.randint(1,6)
  chances[result-n] += 1

for i in range(times):
  throw(n)


print(chances)
