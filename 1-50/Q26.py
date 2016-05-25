#Reciprocal cycles
#Problem 26
#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

#1/2	= 	0.5
#1/3	= 	0.(3)
#1/4	= 	0.25
#1/5	= 	0.2
#1/6	= 	0.1(6)
#1/7	= 	0.(142857)
#1/8	= 	0.125
#1/9	= 	0.(1)
#1/10	= 	0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

import time

from decimal import *
getcontext().prec = 1500 #or 1500

max_num = 0
max_repeat = 0
for i in range(2, 1000):
    quot = Decimal(1) / Decimal(i)
    quot_str = str(quot)
    length = len(quot_str)
    if length > 1000:
        start_index = 2
        a = start_index
        b = start_index + 1 
        while a < (start_index + 5): # a = 2 / 3 / 4 / 5 / 6
            if quot_str[a] == quot_str[b] and quot_str[a+1] == quot_str[b+1] and quot_str[a+2] == quot_str[b+2]: #Check for 3 character matches
                break
            else:
                b += 1
                if b == length - 2:
                    a += 1
                    b = a + 1
        repeat = b - a
        if repeat > max_repeat:
            max_repeat = repeat
            max_num = i
        
print('Number of digits in repetition: ' + str(max_repeat) + '; d: ' + str(max_num))             
 
