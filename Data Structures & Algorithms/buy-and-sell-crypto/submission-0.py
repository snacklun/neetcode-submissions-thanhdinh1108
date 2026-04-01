class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i,value_buy in enumerate(prices):
            temp1 = i
            for j in range(temp1+1,len(prices)):
                temp = prices[j] - value_buy
                if(temp > max_profit):
                    max_profit = temp
        return max_profit
        