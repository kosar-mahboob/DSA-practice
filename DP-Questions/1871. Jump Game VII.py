class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        # reachable[i] indicates whether we can reach index i
        reachable = [False] * n
        reachable[0] = True
        
        # prefix sum of reachable array: pref[i] = number of reachable indices in [0, i-1]
        pref = [0] * (n + 1)
        pref[1] = 1  # reachable[0] is True
        
        for i in range(1, n):
            if s[i] == '0':
                # The leftmost possible source index to reach i is i - maxJump
                left = max(0, i - maxJump)
                # The rightmost possible source index is i - minJump
                right = i - minJump
                # If the window is valid and contains at least one reachable index
                if right >= left and right >= 0:
                    if pref[right + 1] - pref[left] > 0:
                        reachable[i] = True
            # update prefix sum
            pref[i + 1] = pref[i] + (1 if reachable[i] else 0)
        
        return reachable[n - 1]
