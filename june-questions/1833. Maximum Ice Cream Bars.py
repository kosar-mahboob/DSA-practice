from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Counting sort: since costs[i] <= 10^5
        max_cost = max(costs) if costs else 0
        freq = [0] * (max_cost + 1)
        for c in costs:
            freq[c] += 1
        
        count = 0
        for price in range(max_cost + 1):
            if freq[price] == 0:
                continue
            # Can we buy all ice creams of this price?
            can_buy = min(freq[price], coins // price)
            count += can_buy
            coins -= can_buy * price
            if coins < price:
                break
        return count
