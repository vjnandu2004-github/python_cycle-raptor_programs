print("a quadratic equation is of the form ax^2+bx+c")
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=((b**2)-4*a*c)
if d==0:
    print("roots are real and equal")
elif d>0:
    print("roots are real and distict")
else:
    print("roots are imaginary")