
class Solution(object):
    def maxProfit(self, prices):

        """ Brute force
        profit = 0
        max_profit = 0

        if len(prices) == 1 or len(prices) == 0:
            return 0

        for i in range(0, len(prices)):
            j = i + 1
            if j < len(prices):
                for j in range(j, len(prices)):
                    profit = prices[j] - prices[i]
                    if profit > max_profit:
                        max_profit = profit

        return max_profit

        """

        if not prices:
            return 0

        min_prices = float('inf')
        max_profit = 0


        for price in prices:

            if price < min_prices:

                min_prices = price

            elif price - min_prices > max_profit:
                max_profit = price - min_prices

        return max_profit





sol = Solution()
print(f" Max profit is : {sol.maxProfit([1,2])}")
print(f" Max profit is : {sol.maxProfit([7,1,5,3,6,4])}")
print(f" Max profit is : {sol.maxProfit([7,6,4,3,1])}")
