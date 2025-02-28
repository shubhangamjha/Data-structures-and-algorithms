def isPalindrom(s: str) -> bool:
    #write the code here
    n = len(s)
    for i in range(n//2):
        if (s[i] != s[n-1-i]):
            break
    return (i == n//2 -1)

    if i == s:
        print(True)
    else:
        False
print(isPalindrom(input()))