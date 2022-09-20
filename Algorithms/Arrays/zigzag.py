'''
Given an array of N distinct integers, transform the array into a zig zag 
sequence by permuting the array elements. A sequence will be called a zig
zag sequence if the first  elements in the sequence are in increasing 
order and the last K elements are in decreasing order, where K = (N+1)/2. 
You need to find the lexicographically smallest zig zag sequence of the 
given array.

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return
'''


def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) - 1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

findZigZagSequence([1, 2, 3, 7, 6, 5, 4], 7)