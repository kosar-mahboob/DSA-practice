import bisect
from typing import List

class Solution:
    def maximumDestroyedWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # Pair robots with their distances and sort by position
        robots_sorted = sorted(zip(robots, distance))
        walls.sort()
        wall_set = set(walls)

        n = len(robots_sorted)
        # Self walls: does a robot stand on a wall?
        self_wall = [1 if pos in wall_set else 0 for pos, _ in robots_sorted]

        # ----- Leftmost segment (before the first robot) -----
        r0, d0 = robots_sorted[0]
        # walls in [r0 - d0, r0)
        left_count = 0
        if r0 - d0 <= r0 - 1:
            lo = bisect.bisect_left(walls, r0 - d0)
            hi = bisect.bisect_left(walls, r0)   # first index >= r0
            left_count = hi - lo

        # ----- Rightmost segment (after the last robot) -----
        r_last, d_last = robots_sorted[-1]
        # walls in (r_last, r_last + d_last]
        right_count = 0
        if r_last + d_last >= r_last + 1:
            lo = bisect.bisect_right(walls, r_last)   # first > r_last
            hi = bisect.bisect_right(walls, r_last + d_last)  # first > r_last+d_last
            right_count = hi - lo

        # DP for the first robot
        # states: 0 = left, 1 = right, 2 = none
        prev = [0, 0, 0]
        prev[0] = left_count + self_wall[0]
        prev[1] = self_wall[0]
        prev[2] = 0

        # Process gaps between consecutive robots
        for i in range(n - 1):
            r_left, d_left = robots_sorted[i]
            r_right, d_right = robots_sorted[i + 1]

            # Find walls strictly between the two robots
            start = bisect.bisect_right(walls, r_left)   # first > r_left
            end = bisect.bisect_left(walls, r_right)     # first >= r_right

            a = b = c = 0
            if start < end:
                # a = number of walls reachable by left robot's right shot
                limit_a = r_left + d_left
                idx_a = bisect.bisect_right(walls, limit_a, lo=start, hi=end) - 1
                a = idx_a - start + 1 if idx_a >= start else 0

                # b = number of walls reachable by right robot's left shot
                limit_b = r_right - d_right
                idx_b = bisect.bisect_left(walls, limit_b, lo=start, hi=end)
                b = end - idx_b

                # overlap of the two intervals
                lo_over = max(r_left + 1, limit_b)
                hi_over = min(limit_a, r_right - 1)
                if lo_over <= hi_over:
                    lo_idx = bisect.bisect_left(walls, lo_over, lo=start, hi=end)
                    hi_idx = bisect.bisect_right(walls, hi_over, lo=start, hi=end) - 1
                    overlap = hi_idx - lo_idx + 1 if hi_idx >= lo_idx else 0
                else:
                    overlap = 0
                c = a + b - overlap

            # DP transition for robot i+1
            curr = [float('-inf'), float('-inf'), float('-inf')]
            for s_curr in range(3):   # 0:L, 1:R, 2:N
                best = float('-inf')
                for s_prev in range(3):
                    # contribution of the gap
                    if s_prev == 1 and s_curr == 0:
                        gain = c
                    elif s_prev == 1:
                        gain = a
                    elif s_curr == 0:
                        gain = b
                    else:
                        gain = 0
                    candidate = prev[s_prev] + gain + (self_wall[i+1] if s_curr != 2 else 0)
                    if candidate > best:
                        best = candidate
                curr[s_curr] = best
            prev = curr

        # Add the rightmost segment for the last robot if it fired right
        answer = max(prev[0], prev[1] + right_count, prev[2])
        return answer
