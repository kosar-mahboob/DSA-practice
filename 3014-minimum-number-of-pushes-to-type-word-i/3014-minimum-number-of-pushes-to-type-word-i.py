class Solution:
    def minimumPushes(self, word: str) -> int:

        n = len(word)
        if n <= 8:
            return n
        pushes = 0
        for i in range(n):
            pushes += (i // 8) + 1
        return pushes