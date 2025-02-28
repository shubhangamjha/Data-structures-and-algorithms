import time

start = time.time()
arr = [1,2,3,1,4]
found = -1

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            found = arr[i]

print(found)
end= time.time()
print(1000*(end-start))