class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        zeros = s.count('0')
        
        # Already all ones
        if zeros == 0:
            return 0
        
        # Special case: k == n (flip all bits each operation)
        if k == n:
            return 1 if zeros == n else -1
        
        # Now n > k
        ans = float('inf')
        
        # ---- even number of operations: t = 2*m ----
        if zeros % 2 == 0:
            # lower bound from total flips: 2*k*m >= zeros
            m_total = (zeros + 2*k - 1) // (2*k)
            # lower bound from parity‑capacity inequality
            m_bound = (zeros + 2*(n - k) - 1) // (2*(n - k))
            m = max(m_total, m_bound)
            ans = min(ans, 2 * m)
        
        # ---- odd number of operations: t = 2*m + 1 ----
        if (k % 2) == (zeros % 2):
            # lower bound from total flips: k*(2*m+1) >= zeros
            if zeros <= k:
                L_total = 0
            else:
                L_total = (zeros - k + 2*k - 1) // (2*k)   # = (zeros + k - 1)//(2k)
            
            # lower bound from parity‑capacity inequality
            if k <= zeros:
                L_bound = 0
            else:
                L_bound = (k - zeros + 2*(n - k) - 1) // (2*(n - k))
            
            m = max(L_total, L_bound)
            ans = min(ans, 2 * m + 1)
        
        return -1 if ans == float('inf') else ans
