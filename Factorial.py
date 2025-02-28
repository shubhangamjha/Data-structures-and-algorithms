# fatorial of a number

def Factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

print(Factorial(3))