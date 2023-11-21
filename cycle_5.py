def print_all_substrings(s):
    n = len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            print(s[i:j])

def print_substrings_of_length_k(s, k):
    n = len(s)
    if k<=0 or k>n:
        print("Invalid length.")
        return

    for i in range(n-k+1):
        substring = s[i:i +k]
        print(substring)

def print_substrings_length_k_distinct_chars(s, k):
    n = len(s)
    if k<=0 or k>n:
        print("Invalid length.")
        return

    for i in range(n-k+1):
        substring = s[i:i +k]
        if len(set(substring)) == k:
            print(substring)

def print_max_length_substrings_distinct_chars(s, n):
    max_length = 0
    max_substrings = []

    for i in range(len(s)):
        chars_set = set()
        current_length = 0
        current_substring = ""

        for j in range(i, len(s)):
            if s[j] not in chars_set:
                chars_set.add(s[j])
                current_length += 1
                current_substring += s[j]
            else:
                break

        if current_length > max_length:
            max_length = current_length
            max_substrings = [current_substring]
        elif current_length == max_length:
            max_substrings.append(current_substring)

    print("Maximum length substrings with {} distinct characters:".format(n))
    for substring in max_substrings:
        print(substring)

def is_palindrome(s):
    return s == s[::-1]

def print_palindrome_substrings(s):
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                print(substring)


input_string = input("Enter a string: ")

print("All possible substrings:")
print_all_substrings(input_string)

length_k = int(input("Enter the length of substrings (K): "))
print(f"All possible substrings of length {length_k}:")
print_substrings_of_length_k(input_string, length_k)

length_k_distinct = int(input("Enter the length of substrings (K) with N distinct characters: "))
print(f"All substrings of length {length_k_distinct} with {length_k_distinct} distinct characters:")
print_substrings_length_k_distinct_chars(input_string, length_k_distinct)

distinct_chars = int(input("Enter the number of distinct characters (N): "))
print_max_length_substrings_distinct_chars(input_string, distinct_chars)

print("All palindrome substrings:")
print_palindrome_substrings(input_string)
