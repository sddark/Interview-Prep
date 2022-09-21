def maxMin(k, arr):
    # Write your code here
    arr.sort()
    if k == len(arr):
        return arr[k-1]-arr[0]
    else:
        j = k-1
        min = arr[j]-arr[0]
        for i in range(0,len(arr)-j):
            if arr[i+j] - arr[i] < min: 
                min = arr[i+j] - arr[i]
    
    return min

print(maxMin(2, [7,3,10,100,300,200,1000,20,30]))