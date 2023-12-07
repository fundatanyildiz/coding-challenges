class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # i = j = 0
        # while i < len(s) and j < len(t):
        #     if len(s) == 1 and s[i] == t[j]:
        #         return True
        #     elif len(s) == 1 and s[i] != t[j]:
        #         j += 1
        #     elif s[i] == t[j]:
        #         j += 1
        #         i += 1
        #     else:
        #         j += 1
        #
        # if i == len(s):
        #     return True
        # else:
        #     return False
        if len(s) == 0: return True
        i = j = 0
        while len(s) == 1 and j < len(t):
            if s[i] == t[j]:
                return True
            else:
                j += 1

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        if i == len(s):
            return True
        else:
            return False


obj = Solution()
s = "bc"
t = "abc"
print(obj.isSubsequence(s, t))
