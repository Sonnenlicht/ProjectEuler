#Integer right triangles
#Problem 39
#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

#{20,48,52}, {24,45,51}, {30,40,50}

#For which value of p ≤ 1000, is the number of solutions maximised?

def isRightTriangle(x, y, z):
    c = max(x, y, z)
    a = min(x, y, z)
    b = (x+y+z) - (c+a)

    if a**2 + b**2 == c**2:
        return True
    else:
        return False

mydict = {}

for i in range(1, 1001):
    mydict[i] = 0

for a in range(1, 1001):
    for b in range(a+1, 1001):
        #for c in range(1, 1001):
        c = int((a ** 2 + b ** 2) ** 0.5)
        if isRightTriangle(a, b, c) == True:
            perimeter = a+b+c
            if perimeter <= 1000:
                mydict[perimeter] += 1

max_val = 0
max_key = 0
for k, v in mydict.items():
    if v > max_val:
        max_val = v
        max_key = k

print(max_key, max_val)
        
    
            
    
    

    

