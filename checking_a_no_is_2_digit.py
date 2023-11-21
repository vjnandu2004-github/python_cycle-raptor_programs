n=int(input("enter a number:"))
count=0
x=n
dig=0
while x!=0:
    dig=x%10
    x//=10
    count+=1
print("the number of digits of the number is {}".format(count))


    

