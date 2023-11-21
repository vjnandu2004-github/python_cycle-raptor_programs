yr=int(input("enter year:"))
if yr%100==0:
    if yr%400==0:
        print("it is a leap yr")
    else:
        print("it is not leap yr")
else:
    if yr%4==0 :
        print("it is a leap yr")
    else:
        print("it is not a leap year")
