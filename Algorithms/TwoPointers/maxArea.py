'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.'''

'''
Brute force
def maxArea(height: list[int]) -> int:
    temp_area = 0

    for i in range(len(height)-1):
        for j in range(i+1, len(height)):
            if (j - i) * min(height[i], height[j]) > temp_area:
                temp_area = (j - i) * min(height[i], height[j])

    return(temp_area)
'''
# Two Pointer

def maxArea(height: list[int]) -> int:
    temp_area = 0
    left_edge = 0
    right_edge = len(height) - 1

    while left_edge != right_edge:
        if (right_edge - left_edge) * min(height[left_edge], height[right_edge]) > temp_area:
                temp_area = (right_edge - left_edge) * min(height[left_edge], height[right_edge])

        if height[right_edge] < height[left_edge]:
            right_edge -= 1
        else:
            left_edge += 1
    
    return(temp_area)

print(maxArea([1,8,6,2,5,4,8,3,7]))