class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_word = ''
        space = s.count(" ")
        l = len(s)
        for index, i in enumerate(s):
            if not i.isspace():
                last_word += i
            else:
                if space != 0 and index + space != l:
                    space -= 1
                    last_word = ''
                else:
                    return len(last_word)

        return len(last_word)


a = Solution()
s = "   fly me   to   the moon  "
print(a.lengthOfLastWord(s))
