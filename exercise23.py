class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map = {}
        for index, i in enumerate(s):
            if i not in map:
                if t[index] in map.values():
                    return False
                map[i] = t[index]
            else:
                if map[i] != t[index]:
                    return False
                continue
            return True

        # map1 = []
        # map2 = []
        # for idx in s:
        #     map1.append(s.index(idx))
        # for idx in t:
        #     map2.append(t.index(idx))
        # print(map1)
        # print(map2)
        # if map1 == map2:
        #     return True
        # return False


obj = Solution()
s = "egg"
t = "add"
print(obj.isIsomorphic(s, t))
