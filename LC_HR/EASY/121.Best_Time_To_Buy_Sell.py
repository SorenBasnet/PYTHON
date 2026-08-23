
class Solution(object):
    def maxProfit(self, prices):

        profit = 0
        max_profit = 0

        prices.sort()
        return prices[len(prices) - 1] - prices[0]

"""
        for i in range(0, len(prices)):
            for j in range(i, len(prices)):
                profit = prices[i] - prices[j]
                print (f"Value of j is {j} when value of i is {i} then profit is {profit}")

             if profit < max_profit:
                    max_profit = profit

        return -max_profit

"""

#            if i < len(prices) - 1:
#                if prices[i+1] - prices[i] < profit:
#                    profit = prices[i+1] - prices[i]

#        return (-1)*profit




sol = Solution()
print(f" Max profit is : {sol.maxProfit([1,2])}")
