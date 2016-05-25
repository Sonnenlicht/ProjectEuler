#Pandigital multiples
#Problem 38
#Take the number 192 and multiply it by each of 1, 2, and 3:

#192 × 1 = 192
#192 × 2 = 384
#192 × 3 = 576
#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

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

max_num = 0
for a in range(1, 100000):
    for b in range(2, 15):
        mystr = ''
        for c in range(1, b+1):
            product = a * c
            mystr += str(product)
        #print(mystr)
        if isPanDigital(mystr) == True:
            if int(mystr) > max_num:
                max_num = int(mystr)

print(max_num)
            
        
