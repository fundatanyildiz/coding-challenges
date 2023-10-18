class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_set = set(nums)
        n = len(nums)
        for i in my_set:
            count = 0
            for j in nums:
                if j == i:
                    count += 1
                else:
                    continue
            if count > (n//2):
                return i
            else:
                continue


s = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
result = s.majorityElement(nums)
print(result)
