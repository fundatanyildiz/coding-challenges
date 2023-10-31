class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        l = len(nums)
        for i in range(l - 1):
            if nums[i] == nums[i + 1]:
                count += 1
                if count >= 2:
                    nums[i] = 10001
                    count -= 1
            else:
                count = 0
                continue

        k = l - nums.count(10001)
        nums.sort()
        return k


nums = [0, 0, 1, 1, 1, 2, 3, 3]
a = Solution()
print(a.removeDuplicates(nums))
