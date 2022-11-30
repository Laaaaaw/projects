#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc

a = 0
b = 0
c = 0

as1 = 0
bs1 = 0
cs1 = 0

limit = 1000

for a in range(1,limit):
    for b in range(1,limit):
        c = limit - a - b
        if((a**2) + (b**2) == (c**2)):
            as1 = a
            bs1 = b
            cs1 = c

product = as1*bs1*cs1

print(product)