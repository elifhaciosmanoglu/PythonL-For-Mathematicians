import math
print("Enter the coefficients of the form ax^3 + bx^2 + cx + d")
lst=[]
for k in range(0,4):
    m=int(input("Enter coefficient:\n(press enter each time you enter a coefficient)\n"))
    lst.append(m)
x=int(input("Enter the value of x:\n"))
sum1=0
j=3
for k in range(0,3):
    while(j>0):
        sum1=sum1+(lst[k]*math.pow(x,j))
        break
    j=j-1
sum1=sum1+lst[3]
print("The value of the polynomial is:",sum1)
