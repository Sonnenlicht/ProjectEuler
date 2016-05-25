#Smallest multiple
#Problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def gcd(a, b):
    temp = 0
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def lcm(a, b):
    return (a * b) / gcd(a, b)

def lcmm(numlist):
    if len(numlist) == 2:
        return lcm(numlist[0], numlist[1])
    else:
        a = numlist[0]
        numlist[0:] = numlist[1:]
        return lcm(a, lcmm(numlist))
      
numlist = []
for i in range(1, 21):
    numlist.append(i)
print(lcmm(numlist))

