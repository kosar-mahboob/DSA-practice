class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []  # (free_time, weight, index)
        ans = []
        time = 0

        for j, t in enumerate(tasks):
            time = max(time, j)
            # release servers that finished by 'time'
            while busy and busy[0][0] <= time:
                ft, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))
            # if no free servers, jump to the next free time
            if not free:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    ft, w, i = heapq.heappop(busy)
                    heapq.heappush(free, (w, i))
            w, i = heapq.heappop(free)
            ans.append(i)
            heapq.heappush(busy, (time + t, w, i))

        return ans