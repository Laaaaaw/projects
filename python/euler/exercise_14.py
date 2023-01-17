
#Which starting number, under one million, produces the longest chain?

def length(num):
    iteraciones = 1
    while(num > 1):
        if(num%2 == 0):
            num = num/2
        else:
            num = (num * 3) + 1

        iteraciones += 1

    return iteraciones
    
    
limit = 1000000

solution = 0

max_length = 0

for i in range(limit):
    len = length(i) 
    if(len > max_length):
        max_length = len
        solution = i
    
print(solution)