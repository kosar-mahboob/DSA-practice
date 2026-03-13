class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Each worker i: time to reduce by x = workerTimes[i] * (x*(x+1)/2)
        # Binary search on total time T
        # For each T, check if total height reduction >= mountainHeight
        
        def can_reduce(T):
            total = 0
            for t in workerTimes:
                # Find max x such that t * x*(x+1)/2 <= T
                # Binary search within each worker
                left, right = 0, mountainHeight
                while left <= right:
                    mid = (left + right) // 2
                    if t * mid * (mid + 1) // 2 <= T:
                        left = mid + 1
                    else:
                        right = mid - 1
                total += right
                if total >= mountainHeight:
                    return True
            return total >= mountainHeight
        
        left, right = 0, max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        while left < right:
            mid = (left + right) // 2
            if can_reduce(mid):
                right = mid
            else:
                left = mid + 1
        return left
