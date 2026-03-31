from typing import List

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        L = n + m - 1                     # length of the generated string
        
        # ---------- 1. process T constraints (forced characters) ----------
        forced = [None] * L
        for i in range(n):
            if str1[i] == 'T':
                for d in range(m):
                    pos = i + d
                    if forced[pos] is None:
                        forced[pos] = str2[d]
                    elif forced[pos] != str2[d]:
                        return ""        # conflict
        
        # ---------- 2. initialise data for F intervals ----------
        free_cnt = [0] * n                # number of free positions in the interval
        satisfied = [False] * n           # whether the interval is already satisfied
        
        for i in range(n):
            if str1[i] == 'F':
                sat = False
                free = 0
                for d in range(m):
                    pos = i + d
                    if forced[pos] is not None:
                        if forced[pos] != str2[d]:
                            sat = True
                            break
                    else:
                        free += 1
                if sat:
                    satisfied[i] = True
                    continue
                if free == 0:
                    return ""             # forced to be str2 -> impossible
                free_cnt[i] = free
        
        # ---------- 3. build the answer greedily ----------
        ans = [''] * L
        for pos in range(L):
            if forced[pos] is not None:
                ans[pos] = forced[pos]
                continue
            
            # find characters that are forbidden (would make a critical interval impossible)
            forbidden = set()
            left = max(0, pos - m + 1)
            right = min(pos, n - 1)
            for i in range(left, right + 1):
                if str1[i] == 'F' and not satisfied[i]:
                    req = str2[pos - i]          # required char at this position for interval i
                    if free_cnt[i] == 1:
                        forbidden.add(req)
            
            # choose the smallest possible character
            ch = 'a'
            while ch in forbidden:
                ch = chr(ord(ch) + 1)
            ans[pos] = ch
            
            # update the intervals that contain this position
            for i in range(left, right + 1):
                if str1[i] == 'F' and not satisfied[i]:
                    req = str2[pos - i]
                    if ch == req:
                        free_cnt[i] -= 1
                    else:
                        satisfied[i] = True
        
        return ''.join(ans)
