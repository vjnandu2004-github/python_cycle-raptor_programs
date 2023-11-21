b=int(input("enter binary number with only zeros and ones:"))
z=0
binary=b
count=0
dig=0
while binary!=0:
    dig=binary%10
    z=z+dig*(2**count)
    
    binary//=10
    count+=1
print(z)

