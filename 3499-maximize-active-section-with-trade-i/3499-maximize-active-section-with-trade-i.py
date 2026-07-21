class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
 
        total_ones = s.count('1')
        if total_ones == len(s):
            return len(s)
        
        t = '1' + s + '1'
        m = len(t)
        
        max_gain = 0
        
        i = 0
        while i < m:
            if t[i] == '1':
                start = i
                while i < m and t[i] == '1':
                    i += 1
                end = i - 1
                
                # Check if this block is surrounded by '0's
                if start > 0 and end < m - 1 and t[start-1] == '0' and t[end+1] == '0':
                    # Count zeros before
                    zero_before = 0
                    j = start - 1
                    while j >= 0 and t[j] == '0':
                        zero_before += 1
                        j -= 1
                    
                    # Count zeros after
                    zero_after = 0
                    j = end + 1
                    while j < m and t[j] == '0':
                        zero_after += 1
                        j += 1
                    
                    # Gain from this trade = zeros_before + zeros_after
                    max_gain = max(max_gain, zero_before + zero_after)
            else:
                i += 1
        
        return total_ones + max_gain
        
        return total_ones + max(0, max_gain)