#Sum square difference
#Problem 6
#The sum of the squares of the first ten natural numbers is,

#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,

#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def SumofSquares(num):
    total = 0
    for i in range(1, num + 1):
        total += (i * i)
    return total

def SquareofSum(num):
    total = num * (num + 1) / 2
    return total * total

def SumSqDiff(num):
    return SquareofSum(num)-SumofSquares(num)

print(SumSqDiff(10))
print(SumSqDiff(100))
