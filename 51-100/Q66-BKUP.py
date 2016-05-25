#Diophantine equation
#Problem 66
#Consider quadratic Diophantine equations of the form:

#x2 – Dy2 = 1

#For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

#It can be assumed that there are no solutions in positive integers when D is square.

#By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

#32 – 2×22 = 1
#22 – 3×12 = 1
#92 – 5×42 = 1
#52 – 6×22 = 1
#82 – 7×32 = 1

#Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

#Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

import math

def isSqrNum(num):
    root = int(math.sqrt(num))
    if num != root ** 2:
        return False
    return True

def DPh_List(num):
    d_list = []
    for i in range(num+1):
        if isSqrNum(i) == False:
            d_list.append(i)

    return d_list

def DPh_Minimum(DPh_List):
    new_D = 0
    max_x = 0
    for DPh in DPh_List:
        y = 1
        soln = 3
        while isSqrNum(soln) != True:
            soln = DPh * (y**2) + 1
            y += 1
        x = int(math.sqrt(soln))
        if max_x < x:
            max_x = x
            new_D = DPh
    return new_D 
        
                  
            
D_List = []
D_List = DPh_List(1000)
print(DPh_Minimum(D_List))
            
        

