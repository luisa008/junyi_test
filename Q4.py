def group(nums):
    output = 0
    nums = sorted(nums)
    for i in range(0, len(nums), 2):
        output += min(nums[i], nums[i+1])
    return output
    
# a = group([6, 2, 6, 5, 1, 2])
# print(a)