class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # count = len(ransomNote)
        # for i in set(ransomNote):
        #     if ransomNote.count(i) <= magazine.count(i):
        #         count -= ransomNote.count(i)
        #     else:
        #         return False
        #
        # if count == 0:
        #     return True

        magazine_map = {}
        for i in magazine:
            if i in magazine_map:
                magazine_map[i] += 1
            else:
                magazine_map[i] = 1

        print(magazine_map)

        for i in ransomNote:
            if i in magazine_map and magazine_map[i] > 0:
                magazine_map[i] -= 1
            else:
                return False

        return True


ransomNote = "aa"
magazine = "ab"
obj = Solution()
print(obj.canConstruct(ransomNote, magazine))
