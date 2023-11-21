def is_happy(num):
    seen_numbers = []

    while num != 1 and num not in seen_numbers:
        seen_numbers.append(num)
        num = sum(int(digit) ** 2 for digit in str(num))

    return num == 1


number = int(input("Enter a number: "))
if is_happy(number):
    print(f"{number} is a happy number.")
else:
    print(f"{number} is not a happy number.")

m = int(input("Enter upper limit: "))
n = int(input("Enter lower limit: "))
for i in range (m,n+1):
    if is_happy(i):
        print(i,end=" ")
N = int(input("Enter N: "))
for j in range (N+1):
    if is_happy(j):
        print(j,end=" ")

