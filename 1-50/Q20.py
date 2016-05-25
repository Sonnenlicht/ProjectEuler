#Factorial digit sum
#Problem 20
#n! means n × (n − 1) × ... × 3 × 2 × 1

#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#Find the sum of the digits in the number 100!

def factorial(num):
    mult = 1
    for n in range(1, num+1):
        mult *= n
    return mult

def digitsum(num):
    numstr = str(factorial(num))
    total = 0
    for char in numstr:
        total += int(char)
    print(total)
        
digitsum(100)
