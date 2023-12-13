class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        sword = s.split()
        if len(pattern) != len(sword): return False
        map = {}
        for p, i in zip(pattern, sword):
            if p not in map:
                if i in map.values():
                    return False
                else:
                    map[p] = i
            else:
                if map[p] != i:
                    return False
        return True


pattern = "abba"
s = "dog dog cat dog"
obj = Solution()
print(obj.wordPattern(pattern, s))
