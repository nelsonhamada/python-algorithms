def find_duplicate(nums):
    result = False
    nums.sort()
    for index in range(0, len(nums) - 1):
        if isinstance(nums[index], str) or nums[index] < 0:
            result = False
            break
        if nums[index] == nums[index + 1]:
            result = nums[index]
            break
    return result
