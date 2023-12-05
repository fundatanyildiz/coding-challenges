class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # organized_s = [i.capitalize() for i in s if not i.isspace() and i.isalnum()]
        # print(organized_s)
        # if organized_s == organized_s[::-1]:
        #     return True
        # else:
        #     return False
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                print(s[left])
                left += 1
            elif not s[right].isalnum():
                print(s[right])
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True


s1 = "A man, a plan, a canal: Panama"
# s2 = "race a car"
# s3 = "0P"
obj = Solution()
print(obj.isPalindrome(s1))
# print(obj.isPalindrome(s2))
# print(obj.isPalindrome(s3))
