def is_prime(num):
    i = 2
    while i <= num // 2:
        if num % i == 0:
            return False
        i += 1
    return True

def get_primes(N):
    plist = []
    for i in range(N + 1):
        if is_prime(i):
            plist.append(i)
    return plist

N = int(input("Enter the upper limit: "))
prime_list = get_primes(N)
print(prime_list)