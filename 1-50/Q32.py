#Pandigital products
#Problem 32
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

def isPanDigital(mystr):
    strdict = {'0':0, '1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for char in mystr:
        strdict[char] = strdict[char] + 1
    #print(strdict)
    for k, v in strdict.items():
        if k != '0':
            if v != 1:
                return False
    if strdict['0'] != 0:
        return False
    return True

myStr = ''
mySet = {0}

for a in range(10000):
    for b in range(1000):
        product = a * b
        myStr = str(product) + str(a) + str(b)
        #print(myStr)
        if isPanDigital(myStr) == True:
            mySet.add(product)
            #print(str(a) + ' X ' + str(b) + ' = ' + str(product))

mySet = mySet.union(mySet)
#print(mySet)

total = 0
for num in mySet:
    total += num

print(total)


        
