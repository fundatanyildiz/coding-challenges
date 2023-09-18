class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}

        for i in s:
            if i in pairs.keys():
                # add opening brackets to stack
                stack.append(i)
            else:
                # if i is a closet bracket
                if len(stack) == 0:
                    return False
                else:
                    # if stack is not empty check the last inserted item is an opening for i
                    for key, value in pairs.items():
                        if stack[len(stack) - 1] == key and i != value:
                            return False
                        elif stack[len(stack) - 1] == key and i == value:
                            stack.pop()
                            break
        if len(stack) == 0:
            return True
