class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        cp = ""
        for index, i in enumerate(strs[0]):
            count = 1
            for y in range(1, len(strs)):
                if index < len(strs[y]) and i == strs[y][index]:
                    count += 1
            if count == len(strs):
                cp += i
            else:
                break
        if cp is None:
            return " "
        return cp


strs = ["cir", "car"]
a = Solution()
print(a.longestCommonPrefix(strs))
