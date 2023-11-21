#devolp a pgm to read a 4 digit noand find its sum of digits,reverse,
#diffrence bw the product of the integers at odd part and even part

num=int(input("enter a 4 digit no"))
mylst=[]
revnum=0 
while num!=0:
    dig=num%10 
    mylst.append(dig)

    revnum=revnum*10 + dig 
    num=num//10 
print("reverse:", revnum)
sum=0
for j in mylst:
    sum+=j
print("sum:",sum)
print("diffrence between the integers")
print(mylst[0]*mylst[2]-mylst[1]*mylst[3])

