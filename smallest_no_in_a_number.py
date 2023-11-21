n=int(input("enter number:"))
mylst=[]
x=n
dig=0
while x!=0:
    dig=x%10
    x//=10
    mylst.append(dig)
y=min(mylst)
print(y)

     