def peakElement(self,arr, n):
    max_value = -1
    max_index = -1
    for index in range(0, len(arr)):
        if arr[index] > max_value:
            max_value = arr[index]
            max_index = index
                
    return max_index

print(peakElement([404, 652, 755, 400, 933, 61, 677, 369, 740, 1], 10))