def find_index(nums, target):
    # 使用二分搜（O(logn)）
    index = len(nums) // 2
    left = 0
    right = len(nums)
    while True:
        index = (left + right) // 2
        if nums[index] == target:
            return index
        if right == left or right == left+1:
            return -1
        if nums[index] > target:
            right = index
        elif nums[index] < target:
            left = index
            
# a = find_index([1, 2, 3, 6, 7, 8, 14, 23, 56], 23)
# print(a)