from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        # balloon: b:1, a:1, l:2, o:2, n:1
        return min(cnt['b'], cnt['a'], cnt['l'] // 2, cnt['o'] // 2, cnt['n'])
