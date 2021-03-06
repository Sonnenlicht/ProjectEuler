#Sub-string divisibility
#Problem 43
#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

#d2d3d4=406 is divisible by 2
#d3d4d5=063 is divisible by 3
#d4d5d6=635 is divisible by 5
#d5d6d7=357 is divisible by 7
#d6d7d8=572 is divisible by 11
#d7d8d9=728 is divisible by 13
#d8d9d10=289 is divisible by 17
#Find the sum of all 0 to 9 pandigital numbers with this property.

import itertools
numlist = ['0','1','2', '3', '4', '5', '6', '7', '8', '9']
permutations_str = list(itertools.permutations(numlist))

string_list = []
for num in range(len(permutations_str)):
    newstr = ''
    for element in range(len(numlist)):
        newstr += permutations_str[num][element]
    if newstr[0] != '0':
        string_list.append(newstr)

total = 0

for numstr in string_list:
    #numstr = str(num)
    if int(numstr[1:4]) % 2 == 0 and int(numstr[2:5]) % 3 == 0 and int(numstr[3:6]) % 5 == 0 and int(numstr[4:7]) % 7 == 0 and int(numstr[5:8]) % 11 == 0 and int(numstr[6:9]) % 13 == 0 and int(numstr[7:]) % 17 == 0:
        total += int(numstr)
    
print(total)

#def isPanDigital(mystr):
#    length = len(mystr)
#
#    if length != 10:
#        return False
    
    #for char in mystr:
    #    if int(char) > length:
    #        return False
    
    #strdict = {}
    #for i in range(0, 10):
    #    strdict[str(i)] = 0
    #print(strdict)
    
    #for char in mystr:
    #    strdict[char] = strdict[char] + 1
    #print(strdict)
    #for k, v in strdict.items():
    #    if v != 1:
    #        return False
    
    #return True
