class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if need1 > need2:
            cost1, cost2 = cost2, cost1
            need1, need2 = need2, need1

        def total(b):
            return b * costBoth + max(0, need1 - b) * cost1 + max(0, need2 - b) * cost2

        return min(total(0), total(need1), total(need2))