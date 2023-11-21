num=int(input("Enter the number:"))
revnum=0 
while num!=0:
    dig=num%10 
    revnum=revnum*10 + dig 

    num=num//10 
print("Reversed Number =",revnum)
if revnum==num:
    print("It is a palindrome")
else:
    print("it is not a palindrome")