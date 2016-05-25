#Permuted multiples
#Problem 52
#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def digitdict(mystr):
    length = len(mystr)
     
    strdict = {}
    for i in range(0, 10):
        strdict[str(i)] = 0
    #print(strdict)
    
    for char in mystr:
        strdict[char] = strdict[char] + 1

    return strdict

for num in range(100000, 1000000):
    dict_1 = digitdict(str(num * 1))
    dict_2 = digitdict(str(num * 2))
    dict_3 = digitdict(str(num * 3))
    dict_4 = digitdict(str(num * 4))
    dict_5 = digitdict(str(num * 5))
    dict_6 = digitdict(str(num * 6))
    if dict_1 == dict_2 and dict_3 == dict_4 and dict_5 == dict_6:
        if dict_1 == dict_3 and dict_1 == dict_5:
            print(num)
