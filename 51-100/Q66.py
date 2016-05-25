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

def min_m(a, b, k, num):
    min_m = 1
    t = 1
    m = 0
    val_curr = abs(m ** 2 - num)
    val_prev = val_curr + 1
    while val_curr < val_prev:
        val_prev = val_curr
        val_curr = abs(m ** 2 - num)
        m = abs(k) * t + 1
        t += 1
        #print(val_curr, val_prev, m)

    m = abs(k) * (t - 1) + 1
    return m

#Chakravala Method
def Pell(num):
    a = round(math.sqrt(num))
    b = 1
    k = (a ** 2 - num * (b ** 2))
    print(a,b,k)
    print(min_m(a, b, k, num))
    m = min_m(a, b, k, num)
    a_new = int((a * m + num * b) / abs(k))
    b_new = int((a + m * b) / abs(k))
    k_new = int((m ** 2 - num)/k)
    a = a_new
    b = b_new
    k = k_new
    print(a,b,k)
    print(min_m(a, b, k, num))
    m = min_m(a, b, k, num)
   
Pell(53)
           
#D_List = []
#D_List = DPh_List(1000)
#print(DPh_Minimum(D_List))
#print(sqrfract(2))           
        

