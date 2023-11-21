N=int(input("Enter the Number:"))
fact=1 
i=1 
while i<=N:
    fact*=i 
    i+=1
print("Factorial of {} is {}".format(N,fact))