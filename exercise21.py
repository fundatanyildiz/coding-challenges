class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = j = 0
        while i < len(needle) and j < len(haystack) - len(needle) + 1:
            if i == 0 and needle == haystack[j:len(needle) + j]:
                return j
            elif i == 0 and needle != haystack[j:len(needle) + j]:
                j += 1
            elif needle == haystack[j:len(needle) + j]:
                return j
            else:
                j += 1

        return -1

        # for i in range(0, len(haystack)-len(needle)+1):
        #     if haystack[i:len(needle)+i] == needle:
        #         return i
        # return -1


haystack = "leetcode"
needle = "leet0"
obj = Solution()
print(obj.strStr(haystack, needle))
