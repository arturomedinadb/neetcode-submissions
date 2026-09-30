class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        for i in range(len(prices)-1):
            for j in range(i, len(prices)-1):
                new_p = prices[j+1] - prices[i] 
                max_p = max(max_p, new_p)
        if max_p <= 0:
            return 0
        else:
            return max_p
            

