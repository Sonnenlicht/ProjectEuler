#Lexicographic permutations
#Problem 24
#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import itertools
numlist = ['0','1','2', '3', '4', '5', '6', '7', '8', '9']
permutations_str = list(itertools.permutations(numlist))
#permutations_list.sort()
#print(permutations_str)

string_list = []
for num in range(len(permutations_str)):
    newstr = ''
    for element in range(len(numlist)):
        newstr += permutations_str[num][element]
    string_list.append(newstr)
    
print(string_list[999999])

