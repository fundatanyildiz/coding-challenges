class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t) != len(s): return False
        map = {}
        for i in s:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1
        for i in t:
            if i in map and map[i] > 0:
                map[i] -= 1
            else:
                return False
        return True


s = "ab"
t = "ba"
obj = Solution()
print(obj.isAnagram(s, t))
