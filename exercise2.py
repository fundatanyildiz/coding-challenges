class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        a = len(nums1) - m
        for i in range(0, a):
            nums1.pop(len(nums1) - 1)

        b = len(nums2) - n
        for i in range(0, b):
            nums1.pop(len(nums2) - 1)

        for i in nums2:
            nums1.append(i)
            nums1.sort()
