class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = [0] * 3  # counts of a, b, c
        left = 0
        ans = 0
        
        for right in range(n):
            count[ord(s[right]) - ord('a')] += 1
            
            # When we have all three characters, shrink from left
            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                # All substrings starting from left to right are valid
                ans += n - right
                # Move left pointer forward
                count[ord(s[left]) - ord('a')] -= 1
                left += 1
        
        return ans