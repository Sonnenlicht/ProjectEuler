#Special Pythagorean triplet
#Problem 9
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def isPythoTriplet(x, y, z):
    c = max(x, y, z)
    a = min(x, y, z)
    b = (x+y+z) - (a+c)
    if (a*a + b*b) == c*c:
        return True
    else:
        return False

for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if a + b + c == 1000:
                if isPythoTriplet(a, b, c) == True:
                    print(a*b*c)
                    
