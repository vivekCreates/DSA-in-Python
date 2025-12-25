def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

sorted = selection_sort([10,1,4,7,9,15])
print(sorted)

