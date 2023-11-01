class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if k >= l:
            k = k % l
        if k:
            part1 = [nums[i] for i in range(k + 1, l)]
            nums.append(part1)
            del (nums[0:l - k])

        print(nums)


a = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
a.rotate(nums, k)
