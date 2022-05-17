arr = [1, 2, 3, 4, 5]
reverseArr = []

for i in range(len(arr) - 1, -1, -1):
    reverseArr.append(arr[i])

print(reverseArr)

# Or
arr1 = [44, 22, 11, 0]
print(arr1[::-1])
