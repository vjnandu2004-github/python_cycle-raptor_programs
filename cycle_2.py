import math
a=int(input("enter the saide a"))
b=int(input("enter the saide b"))
c=int(input("enter the saide c"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
perimeter=a+b+c
print(area)
print(perimeter)