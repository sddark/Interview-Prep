def merge(arr):
    if len(arr) <= 1:
        return arr

    arr.sort()
    output_arr = []
    output_arr.append([arr[0][0],arr[0][1]])

    for i in range(len(arr)-1):
        a = len(output_arr)

        if output_arr[a-1][1] >= arr[i+1][0] and output_arr[a-1][1] < arr[i+1][1]:
            output_arr[a-1][1] = int(arr[i+1][1])
        elif output_arr[a-1][1] >= arr[i+1][1]:
            pass
        else:
            output_arr.append([arr[i+1][0],arr[i+1][1]])

    return output_arr


print(merge([[1,3],[2,6],[8,10],[15,18]]))