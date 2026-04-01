from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        # Pair each robot with its original index and sort by position
        robots = sorted(
            [(positions[i], healths[i], directions[i], i) for i in range(n)],
            key=lambda x: x[0]
        )
        stack = []          # each element: [health, original_index]
        survivors = []      # each element: (original_index, health)

        for pos, health, d, idx in robots:
            if d == 'R':
                stack.append([health, idx])
            else:  # d == 'L'
                alive = True
                while stack and alive:
                    r_health, r_idx = stack[-1]
                    if r_health > health:
                        # right robot survives with health decreased by 1
                        stack[-1][0] -= 1
                        alive = False  # left robot dies
                    elif r_health < health:
                        # left robot survives with health decreased by 1
                        health -= 1
                        stack.pop()   # right robot dies
                        # continue while loop to check next right robot
                    else:  # equal health
                        stack.pop()   # both die
                        alive = False
                if alive:
                    survivors.append((idx, health))

        # Add all remaining right‑moving robots from stack
        for health, idx in stack:
            survivors.append((idx, health))

        # Sort by original index to preserve input order
        survivors.sort(key=lambda x: x[0])
        return [health for _, health in survivors]
