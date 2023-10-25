class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        buying = prices[0]
        for selling in prices[1:]:
            if selling - buying > 0:
                profit = max(profit, selling - buying)
            else:
                buying = selling

        return profit


s = Solution()
prices = [900, 510, 174, 329, 873, 382, 279, 855, 396, 810, 322, 192, 442, 775, 445, 861, 303, 975, 478, 543, 87, 875,
          283, 740, 376, 156]
print(s.maxProfit(prices))
