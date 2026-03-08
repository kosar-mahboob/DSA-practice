class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        """
        Returns True if every binary string of length k appears as a substring of s.
        """   
        total = 1 << k 
        # total number of distinct binary strings of length k
        seen = set()
        for i in range(len(s) - k + 1): 
            seen.add(s[i:i+k])
            if len(seen) == total:   # early exit if we've found them all
                return True
        return False
