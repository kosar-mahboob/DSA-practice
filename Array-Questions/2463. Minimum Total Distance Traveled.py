from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])  # sort by position
        
        n = len(robot)
        # dp[i] = minimum distance to repair first i robots using some factories
        dp = [0] + [float('inf')] * n
        
        for pos, limit in factory:
            # Start with current best distances (not using this factory)
            new_dp = dp[:]
            for i in range(1, n + 1):
                dist_sum = 0
                # Try assigning up to 'limit' robots ending at i-1 to this factory
                for k in range(1, min(limit, i) + 1):
                    dist_sum += abs(robot[i - k] - pos)
                    if dp[i - k] + dist_sum < new_dp[i]:
                        new_dp[i] = dp[i - k] + dist_sum
            dp = new_dp
            
        return int(dp[n])
