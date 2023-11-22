def is_happy(num):
    seen_numbers = []

    while num != 1 and num not in seen_numbers:
        seen_numbers.append(num)
        num = sum(int(digit) ** 2 for digit in str(num))

    return num == 1

def check_happiness():
    number = int(input("Enter a number: "))
    if is_happy(number):
        print(number," is a happy number.")
    else:
        print(number," is not a happy number.")

def print_happy_numbers_in_range():
    m = int(input("Enter upper limit: "))
    n = int(input("Enter lower limit: "))
    print("Happy numbers within the given range:")
    for i in range(m, n + 1):
        if is_happy(i):
            print(i, end=" ")

def print_happy_numbers_up_to_N():
    N = int(input("Enter N: "))
    print("Happy numbers up to {}:".format(N))
    for j in range(N + 1):
        if is_happy(j):
            print(j, end=" ")


check_happiness()
print_happy_numbers_in_range()
print_happy_numbers_up_to_N()




