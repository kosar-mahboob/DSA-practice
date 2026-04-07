from typing import List
class Robot:
    def __init__(self, width: int, height: int):
        self.W = width
        self.H = height
        # length of the cycle (after the first step)
        self.L = 2 * (width + height - 2)
        # directions in order: East, North, West, South (left turn)
        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # precompute the cycle of states (position + direction index)
        self.cycle = []
        # start from (1, 0) facing East (state after the first step)
        x, y = 1, 0
        dir_idx = 0  # East
        for _ in range(self.L):
            self.cycle.append((x, y, dir_idx))
            # perform one step
            dx, dy = self.dirs[dir_idx]
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.W and 0 <= ny < self.H:
                x, y = nx, ny
            else:
                # turn left (counter‑clockwise)
                dir_idx = (dir_idx + 1) % 4
                dx, dy = self.dirs[dir_idx]
                x, y = x + dx, y + dy
        self.total_steps = 0

    def step(self, num: int) -> None:
        self.total_steps += num

    def getPos(self) -> List[int]:
        if self.total_steps == 0:
            return [0, 0]
        t = (self.total_steps - 1) % self.L
        x, y, _ = self.cycle[t]
        return [x, y]

    def getDir(self) -> str:
        if self.total_steps == 0:
            return "East"
        t = (self.total_steps - 1) % self.L
        _, _, d = self.cycle[t]
        return ["East", "North", "West", "South"][d]
