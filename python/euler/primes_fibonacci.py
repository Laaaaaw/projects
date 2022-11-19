def primes():
  ListofPrimes = []
  for x in range(1,1000+1):
    if x > 1:
      for i in range(2, x):
        if (x % i) == 0:
        
          break
        
      else:
       ListofPrimes.append(x):

  return ListofPrimes

def fibonacci():
  Fibonacci = []
  first=0
  second=1
  sum=0
  count=1
  while(count<=1000):
    Fibonacci.append(sum)
    count+=1
    first=second
    second=sum
    sum=first+second
  return Fibonacci



FB = fibonacci()
LP = primes()

FB1 = set(FB)
LP1 =set(LP)

Commons = FB1.intersection(LP1)

print(Commons)