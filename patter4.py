def pattern(n):
    l = []
    for i in range(n):
        ans = ''
        for j in range(i+1):
            if j == 0 or j == i:
                ans += '1'
            else:
                ans += '2'

        l.append(ans)

    for i in l:
        print(i)

print(pattern(int(input("Enter the value of n: "))))

