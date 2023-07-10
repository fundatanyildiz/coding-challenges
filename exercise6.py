class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # two dimensional array with zeros
        list_of_lists = [[0 for i in range(numRows)] for j in range(numRows)]
        # iterate rows
        for r in range(0, numRows):
            # iterate for each value of the row
            for k in range(0, r+1):
                # if it is first or list item on the row
                # should be equal 1
                if k==0 or k==r:
                    list_of_lists[r][k] = 1
                else:
                     # k th element of the row r equals
                     # sum of k th and (k-1) th element of previous row
                     list_of_lists[r][k] = list_of_lists[r-1][k-1] + list_of_lists[r-1][k]
        # remove zeros from list_of_lists
        res = [ [item for item in a_list if item != 0] for a_list in list_of_lists]
        return res

obj = Solution()
print(obj.generate(4))