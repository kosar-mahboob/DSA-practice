class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions: north, east, south, west
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0  # start facing north
        x, y = 0, 0
        max_dist_sq = 0

        # Store obstacles in a set for O(1) lookups
        obstacle_set = set(map(tuple, obstacles))

        for cmd in commands:
            if cmd == -2:          # turn left
                dir_idx = (dir_idx + 3) % 4
            elif cmd == -1:        # turn right
                dir_idx = (dir_idx + 1) % 4
            else:                  # move forward
                dx, dy = dirs[dir_idx]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obstacle_set:
                        break
                    x, y = nx, ny
                    max_dist_sq = max(max_dist_sq, x*x + y*y)

        return max_dist_sq
