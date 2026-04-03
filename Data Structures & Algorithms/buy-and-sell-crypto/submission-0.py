class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        T: O(n)
        S: O(1) 

        min
        max_profit

        [10,1,5,6,7,1]

        10
        min = 1
        max_profit = 5- 1= 4
        max_profit = 6- 1 = 5
        max-profit = 7-1 = 6
        maxprofit = 1-1 =0


        [10,8,7,5,2]

        min 2
        max profit 0
        Create min and max profit
        as im iteraring through prices
        ill set the min to the elem there
        if the next element is greater than the min 
        then ill update max profit
        then return mex profit
        """

        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
           min_price = min(min_price, prices[i]) 
           if prices[i] > min_price:
                max_profit = max(max_profit, prices[i] - min_price)

        return max_profit