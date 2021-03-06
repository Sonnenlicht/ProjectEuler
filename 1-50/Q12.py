#Highly divisible triangular number
#Problem 12
#The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#Let us list the factors of the first seven triangle numbers:

# 1: 1
# 3: 1,3
# 6: 1,2,3,6
#10: 1,2,5,10
#15: 1,3,5,15
#21: 1,3,7,21
#28: 1,2,4,7,14,28
#We can see that 28 is the first triangle number to have over five divisors.

#What is the value of the first triangle number to have over five hundred divisors?

import time

# returns the nth triangle number; that is, the sum of all the natural numbers less than, or equal to, n
def triangleNumber(n):
    return sum ( [ i for i in range(1, n + 1) ] )

start = int(round(time.time() * 1000)) # starts the stopwatch

j = 0 # j represents the jth triangle number
n = 0 # n represents the triangle number corresponding to j
numberOfDivisors = 0 # number of divisors for triangle number n

while numberOfDivisors <= 500:

    # resets numberOfDivisors because it's now checking a new triangle number
    # and also sets n to be the next triangle number
    numberOfDivisors = 0
    j += 1
    n = triangleNumber(j)

    # for every number from 1 to the square root of this triangle number,
    # count the number of divisors
    i = 1
    while i <= n**0.5:
        if n % i == 0:
            numberOfDivisors += 1
        i += 1

    # 1 to the square root of the number holds exactly half of the divisors
    # so multiply it by 2 to include the other corresponding half
    numberOfDivisors *= 2

finish = int(round(time.time() * 1000)) # stops the stopwatch

print (n)
print ("Time taken: " + str(finish-start) + " milliseconds")

#def len_factors(number):
#    factors_list =  [n for n in range(1, number + 1) if number % n == 0]
#    print(len(factors_list))
#    return len(factors_list)

#def highTriangle():
#    for i in range(2000, 4000):
#        i = 100000
#        sigma = int(i * (i+1) / 2)
#        print(sigma)
#        if len_factors(sigma) > 500:
#            return sigma

#print(highTriangle())
        
        
