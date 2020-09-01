
def double_nums(nums, i=0):
    if i >= len(nums):
        return nums
    nums[i] = nums[i] * 2
    return double_nums(nums, i + 1)