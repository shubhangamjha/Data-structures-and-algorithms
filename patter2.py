def pattern(n):
    l = []
    for i in range(n+1):
        s=""
        for j in range(n-i):
            s= s + str(j+1)
        l.append(s)
    for i in l:
        print(i)

print(pattern(int(input("Enter the value of n: "))))

