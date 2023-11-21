n=int(input("enter the number:"))
x=n
count=0
while x!=0:
    x//=10
    count+=1
auotom=(n**2)%(10**count)
if auotom==n:
    print("it is automorphic")
else:
    print("not automorphic")
