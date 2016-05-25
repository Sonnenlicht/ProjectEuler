#Digit cancelling fractions
#Problem 33
#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

def reduce(num, den):
    numstr = str(num)
    denstr = str(den)
    if numstr[0] == denstr[0]:
        num = int(numstr[1])
        den = int(denstr[1])
    elif numstr[1] == denstr[1]:
        num = int(numstr[0])
        den = int(denstr[0])
    elif numstr[0] == denstr[1]:
        num = int(numstr[1])
        den = int(denstr[0])
    elif numstr[1] == denstr[0]:
        num = int(numstr[0])
        den = int(denstr[1])

    result = [num, den]
    return result

den_list = []
num_list = []

for a in range(10, 99):
    for b in range(a+1, 100):
        result = reduce(a, b)
        if len(str(result[0])) == 1 and len(str(result[1])) == 1 and result[1] != 0:
            if a/b == result[0]/result[1] and a%10 != 0:
                den_list.append(result[1])
                num_list.append(result[0])
                #print(a, b, result[0], result[1])

product = 1
for i in range(len(num_list)):
    product *= den_list[i]/num_list[i]

print(product)




