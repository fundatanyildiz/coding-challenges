from random import sample

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums


    def reset(self):
        """
        :rtype: List[int]
        """
        return self.nums



    def shuffle(self):
        """
        :rtype: List[int]
        """
        return sample(self.nums, len(self.nums))


list1 = [1, 2, 3]
# Your Solution object will be instantiated and called as such:
obj = Solution(list1)
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_2)
print(param_1)