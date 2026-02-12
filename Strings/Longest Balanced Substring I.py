#leetcode problem no : 3713 Longest Balanced Substring I
class Solution:
    def longestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                freq[idx] += 1
                
                # check if all present frequencies are equal
                common = None
                balanced = True
                for k in range(26):
                    if freq[k] > 0:
                        if common is None:
                            common = freq[k]
                        elif freq[k] != common:
                            balanced = False
                            break
                if balanced:
                    max_len = max(max_len, j - i + 1)
        
        return max_len
