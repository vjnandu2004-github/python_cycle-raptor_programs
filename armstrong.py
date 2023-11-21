n=int(input("enter number:"))
sumdigs=0
x=n
while x!=0:
    dig=x%10
    sumdigs+=dig**3 #cube of each digit added to sumdigs
    x//=10 #truncate temp from the rigth most digit 

if n==sumdigs:
    print("amstrong no")
else:
    ("not amstrong no")