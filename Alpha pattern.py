def alpha_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(ord('A')+i), end='')
        print()

print(alpha_pattern(3))