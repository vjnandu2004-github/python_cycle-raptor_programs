import math
def areaof_triangle(a,b,c):
s=(a+b+c)//2
Area=math.floor(math.sqrt(s*(s-a)*(s-b)*(s-c)))
return Area
mylst=[]
for i in range(1,3):
print("Trinangle-",i)
a=int(input("Enter the side a:"))
b=int(input("Enter the side b:"))
c=int(input("Enter the side c:"))
Area=areaof_triangle(a,b,c)
mylst.append(Area)
print("Area of Triangle 1-",mylst[0])
print("Area of Triangle 2-",mylst[1])
sum_of_area=sum(mylst)
print("Sum of areas of 2 triangles: ",sum_of_area)
ct1=round(((int(mylst[0]))/(sum_of_area))*100,2)
ct2=round(((int(mylst[1]))/(sum_of_area))*100,2)
print("Contribution of triangle 1=",ct1)
print("Contribution of triangle 1=",ct2)
