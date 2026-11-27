class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
    
        n = len(items)
        factors = [f for f, _ in items]
        prices = [p for _, p in items]

        free_gain = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and factors[j] % factors[i] == 0:
                    free_gain[i] += 1

        dp = [0] * (budget + 1)
        for i in range(n):
            p = prices[i]
            gain = 1 + free_gain[i]
            for b in range(budget, p - 1, -1):
                if dp[b - p] + gain > dp[b]:
                    dp[b] = dp[b - p] + gain

        min_price = min(prices)
        ans = 0
        for b in range(budget + 1):
            ans = max(ans, dp[b] + (budget - b) // min_price)
        return ans