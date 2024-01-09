class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0: return []
        if len(nums) == 1: return [str(nums[0])]
        ranges_array = []
        i = count = 0
        while i < len(nums) - 1:
            if nums[i + 1] == nums[i] + 1:
                count += 1
                i += 1
            else:
                if count == 0:
                    ranges_array.append(str(nums[i]))
                    i += 1
                else:
                    ranges_array.append("{}->{}".format(nums[i - count], nums[i]))
                    i += 1
                    count = 0
        while i == len(nums) - 1:
            if nums[i] == nums[i - 1] + 1:
                ranges_array.append("{}->{}".format(nums[i - count], nums[i]))
                i += 1
            else:
                ranges_array.append(str(nums[i]))
                i += 1
        return ranges_array


# nums = [1, 3]
# nums = [0, 1, 2, 4, 5, 7]
nums = [0, 2, 3, 4, 6, 8, 9]

obj = Solution()
print(obj.summaryRanges(nums))
