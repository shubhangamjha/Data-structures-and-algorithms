def pattern(n):
    l = []
    for i in range(n):
        x= i+1
        s=''
        for j in range(i+1):
            s= s + str(x)
            x+=1
        l.append(s)

    for z in l:
        print(z)

print(pattern(int(input("Enter the value of n: "))))

