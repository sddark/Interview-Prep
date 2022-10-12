def largestPerimeter(nums) -> int:

    nums.sort()
    length = len(nums)

    if len(nums) == 3:
        if nums[length-3] + nums[length-2] <= nums[length-1]:
            return 0
        else:
            return nums[length-3] + nums[length-2] + nums[length-1]

    for i in range(0, len(nums)-2):
        if nums[length-i-3] + nums[length-i-2] <= nums[length-i-1]:
            continue
        else:
            return nums[length-i-3] + nums[length-i-2] + nums[length-i-1]
    
    return 0

print(largestPerimeter([3,6,2,3]))