# right sided triangle
"""def RightSided_triangel(n):
    for i in range(n):
        for j in range(i, n-1):
            print(' ', end=" ")
        for j in range(i+1):
            print('*', end=' ')
        print()

print(RightSided_triangel(5))"""


# hill side of n rows
"""def Hill_slide(n):
    for i in range(n):
        for j in range(i, n-1):
            print(' ', end=' ')
        for j in range(i+1):
            print('*', end=' ')
        for j in range(i):
            print('*', end=' ')
        print()
print(Hill_slide(5))"""

# number pattern

"""def numberPattern(n):
    ans=[]
    for i in range(n):
        temp = i+1
        tempStr = ""
        for j in range(i+1):
            tempStr += str(temp)
            temp += 1
        ans.append(tempStr)
    for i in ans:
        print(ih)

print(numberPattern(6))"""

#Diamond of sttrings

def DiamondOfStars(n):
    lowerHillRows = n//2 + 1
    upperHillRows = n//2


    for i in range(upperHillRows):
        for j in range(i, upperHillRows):
            print(' ', end='')

        for j in range(i):
            print('*', end='')

        for j in range(i+1):
            print('*', end='')

        print()

    for i in range(lowerHillRows):
        for j in range(i):
            print(' ', end='')

        for j in range(i, lowerHillRows-1):
            print('*', end='')

        for j in range(i, lowerHillRows):
            print('*', end='')

        print()

print(DiamondOfStars(3))