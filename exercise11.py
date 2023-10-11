def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    count = 0
    for index, i in enumerate(nums):
        if i == val:
            count += 1
            nums[index] = 101
            print(nums)
        else:
            continue
    k = len(nums) - count
    nums.sort()
    return k


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(removeElement(nums, val))
