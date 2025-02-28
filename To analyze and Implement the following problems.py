# Write a code to reverse a number

def reverse_number(n):
    reversed_number = 0
    while n > 0:
        remainder = n % 10
        reversed_number = (reversed_number * 10) + remainder
        n = n // 10
    return reversed_number

# Test the function
print(reverse_number(12345))
print('This code has a time complexity of O(log(n)) \nbecause we are dividing the number by 10 in each iteration.')



# write the code to find the fabonacci series upto n th term

def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Test the function
print(fibonacci(10))
print('This code has a time complexity of O(n) because we are iterating from 2 to n.')




#write a code to checck if the given string is palindrome or not

def is_palindrome(s):
    return s == s[::-1]

# Test the function
print(is_palindrome("madam"))
print('This code has a time complexity of O(n) \nbecause string reversal takes O(n) time where n is the length of the string.')

