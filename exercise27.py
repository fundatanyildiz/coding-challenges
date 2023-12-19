class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map = {}
        index = 0
        while index < len(nums):
            if nums[index] in map and index - map[nums[index]] <= k:
                return True
            map[nums[index]] = index
            index += 1
        return False


nums = [1, 2, 3, 1]
k = 3
obj = Solution()
print(obj.containsNearbyDuplicate(nums, k))
# nums = [1,2,3,1,2,3], k = 2 Output: false
