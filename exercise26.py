class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        map = {'0': 0, '1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81}
        sums_set = set()
        while n != 1:
            sum = 0
            for i in str(n):
                sum += map[i]
            n = sum
            if sum in sums_set:
                return False
            sums_set.add(sum)
        return True


n = 19
obj = Solution()
print(obj.isHappy(n))
