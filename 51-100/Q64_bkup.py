#Odd period square roots
#Problem 64
#All square roots are periodic when written as continued fractions and can be written in the form:

#√N = a0 +	
#1
#	a1 +	
#1
# 	 	a2 +	
#1
# 	 	 	a3 + ...
#For example, let us consider √23:

#√23 = 4 + √23 — 4 = 4 + 	
#1
# = 4 + 	
#1
# 	
#1
#√23—4
# 	1 + 	
#√23 – 3
#7
#If we continue we would get the following expansion:

#√23 = 4 +	
#1
#	1 +	
#1
# 	 	3 +	
#1
# 	 	 	1 +	
#1
# 	 	 	 	8 + ...
#The process can be summarised as follows:

#a0 = 4,	 	
#1
#√23—4
# = 	
#√23+4
#7
# = 1 + 	
#√23—3
#7
#a1 = 1,	 	
#7
#√23—3
# = 	
#7(√23+3)
#14
# = 3 + 	
#√23—3
#2
#a2 = 3,	 	
#2
#√23—3
# = 	
#2(√23+3)
#14
# = 1 + 	
#√23—4
#7
#a3 = 1,	 	
#7
#√23—4
# = 	
#7(√23+4)
#7
# = 8 + 	√23—4
#a4 = 8,	 	
#1
#√23—4
# = 	
#√23+4
#7
# = 1 + 	
#√23—3
#7
#a5 = 1,	 	
#7
#√23—3
# = 	
#7(√23+3)
#14
# = 3 + 	
#√23—3
#2
#a6 = 3,	 	
#2
#√23—3
# = 	
#2(√23+3)
#14
# = 1 + 	
#√23—4
#7
#a7 = 1,	 	
#7
#√23—4
# = 	
#7(√23+4)
#7
# = 8 + 	√23—4
#It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

#The first ten continued fraction representations of (irrational) square roots are:

#√2=[1;(2)], period=1
#√3=[1;(1,2)], period=2
#√5=[2;(4)], period=1
#√6=[2;(2,4)], period=2
#√7=[2;(1,1,1,4)], period=4
#√8=[2;(1,4)], period=2
#√10=[3;(6)], period=1
#√11=[3;(3,6)], period=2
#√12= [3;(2,6)], period=2
#√13=[3;(1,1,1,1,6)], period=5

#Exactly four continued fractions, for N ≤ 13, have an odd period.

#How many continued fractions for N ≤ 10000 have an odd period?
import math
import decimal
iterations = 0
append_list = []
frac_list = []
from decimal import *

def sqrfract(num):
    getcontext().prec = 200
    root = Decimal(num)**Decimal(0.5)
    #root = float(math.sqrt(num))
    a_0 = int(math.sqrt(num))
    den = Decimal(root) - Decimal(a_0)
    a_1 = (Decimal(1)/Decimal(den))
    #print(a_1)
    #a_1 = format(a_1, '.17')
    while len(append_list) < 106:
        append_list.append(a_0)
        sqrfract(Decimal(a_1) ** 2)
    #print(a_0, a_1)
    #print(append_list)
    #return append_list
    return append_list[1:]

def period(fraclist):
    #print(fraclist)
    period = 0
    i = 1
    fracset = set(fraclist[:6])
    fracset = fracset.union(fracset)
    if len(fracset) == 1:
        return 1
    for j in range(2, len(fraclist)):
        if fraclist[i:j] == fraclist[j:2*j-i]:
            if period < (j-i):
                #print('if')
                period = j-i
        elif period > 1:
            break
        else:
            continue
            #print('else')
    return period    

def sqrnum(num):
    root = math.sqrt(num)
    a_0 = int(math.sqrt(num))
    if root - a_0 == 0:
        return True
    return False

total = 0
                    
for num in range(2, 10001):
    if sqrnum(num) != True:
        append_list = []
        #sqrfract(num)
        frac_list = sqrfract(num)
        repeats = period(frac_list)
        #print(repeats)
        if repeats % 2 != 0:
            total += 1

print(total)
        
#print(sqrfract(2))
