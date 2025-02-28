#to implement and analyze the linear sorting algorithm

def counting_sort(array):
    size = len(array)
    output = [0] * size

    count = [0] * 10 # Initialize count array


    for i in range(0, size): # Store the count of each elements in count array
        count[array[i]] += 1



    for i in range(1, 10): # position of this character in output array
        count[i] += count[i - 1] # Change count[i] so that count[i] now contains actual

    # Build the output character array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


# Test the function
data = [4, 2, 2, 8, 3, 3, 1]
counting_sort(data)
print("Sorted Array in Ascending Order: ", data)


print("The time complexity of this algorithm is O(n), where n is the number of elements in the input array. \nThis is because we go through the input array twice - once to count the occurrence of each element and once to sort them")