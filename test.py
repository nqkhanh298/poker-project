arr = [1, 2, 3, 4, 1, 2, 2]
arr2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

list_index = []
for i in range(len(arr)):
    if arr.count(arr[i]) == 2:
        list_index.append(i)
print(list_index)
for index in list_index:
    arr2.pop(index)

print(arr2)