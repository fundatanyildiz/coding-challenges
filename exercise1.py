class Solution(object):
    def remove_duplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # remove duplicates in list
        for i, item in enumerate(nums):
            for y in nums[i + 1:]:
                if item == y:
                    nums.remove(y)
                    continue

        return len(nums)
