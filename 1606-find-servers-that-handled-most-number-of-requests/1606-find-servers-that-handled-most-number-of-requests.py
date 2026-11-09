from typing import List
import heapq
from bisect import bisect_left

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = list(range(k))
        busy = []  # (free_time, server_id)
        count = [0] * k

        for i, t in enumerate(arrival):
            # release servers that finished
            while busy and busy[0][0] <= t:
                _, sid = heapq.heappop(busy)
                # insert sid into free (keep free sorted)
                idx = bisect_left(free, sid)
                free.insert(idx, sid)

            if not free:
                continue

            target = i % k
            # find the first free server >= target, wrapping around
            pos = bisect_left(free, target)
            if pos == len(free):
                pos = 0
            sid = free.pop(pos)
            count[sid] += 1
            heapq.heappush(busy, (t + load[i], sid))

        mx = max(count)
        return [i for i in range(k) if count[i] == mx]