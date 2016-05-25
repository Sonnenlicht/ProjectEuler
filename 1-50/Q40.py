#Champernowne's constant
#Problem 40
#An irrational decimal fraction is created by concatenating the positive integers:

#0.123456789101112131415161718192021...

#It can be seen that the 12th digit of the fractional part is 1.

#If dn represents the nth digit of the fractional part, find the value of the following expression.

#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

numstr = ''

for num in range(1, 200000):
    numstr += str(num)

result = int(numstr[0]) * int(numstr[9]) * int(numstr[99]) * int(numstr[999]) * int(numstr[9999]) * int(numstr[99999]) * int(numstr[999999])
print(result)
