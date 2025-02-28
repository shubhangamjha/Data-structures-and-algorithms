def isPrime(n):
    for i in range (2, int(1+n/2)):
        if n%i == 0:
            return False
        return True

print(isPrime(10))