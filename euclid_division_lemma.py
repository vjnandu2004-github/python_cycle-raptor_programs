a=int(input("enter n1:"))
b=int(input("enter n2:"))
while (a%b!=0):
    rem=a%b
    a , b = b , rem
print(b)
