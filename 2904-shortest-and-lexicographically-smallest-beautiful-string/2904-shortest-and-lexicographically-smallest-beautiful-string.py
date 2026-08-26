class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
       
        n = len(s)
        best = ""
        min_len = n + 1

        for i in range(n):
            ones = 0
            for j in range(i, n):
                if s[j] == '1':
                    ones += 1

                if ones == k:
                    length = j - i + 1
                    sub = s[i:j+1]
                    if length < min_len or (length == min_len and sub < best):
                        best = sub
                        min_len = length
                elif ones > k:
                    break

        return best