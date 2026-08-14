class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)
        left = 0
        ans = 0

        for right, ch in enumerate(s):
            cnt[ch] += 1
            while cnt[ch] > 2:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans