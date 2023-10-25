class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
        return profit

        # profit = 0
        # buying = prices[0]
        # for selling in prices[1:]:
        #     if selling - buying > 0:
        #         profit += (selling - buying)
        #         buying = selling
        #     else:
        #         buying = selling
        # return profit


s = Solution()
prices = [1, 2, 3, 4, 5]
print(s.maxProfit(prices))
