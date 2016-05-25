#Number spiral diagonals
#Problem 28
#Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13

#It can be verified that the sum of the numbers on the diagonals is 101.

#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

#1, 3, 5, 7, 9, 13, 17, 21, 25........

def spiralDiagSum(num):
    total = 0
    rval = 1
    lval = 1
    for i in range(num):
        rval += 2 * (i)
                        
        if i%2 == 0:
            lval += 4 * (i/2)
        else:
            lval += 4 * (i+1)/2

        total += (int(lval) + rval)
        #print(int(lval), rval)
        
    return total - 1

print(spiralDiagSum(1001)) 
    
