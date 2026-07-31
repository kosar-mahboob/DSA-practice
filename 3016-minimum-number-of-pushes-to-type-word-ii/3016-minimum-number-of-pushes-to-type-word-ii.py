class Solution:
    def minimumPushes(self, word: str) -> int:
        
        # Count frequency of each character
        freq = Counter(word)
        # Sort frequencies in descending order
        freq_values = sorted(freq.values(), reverse=True)
        
        pushes = 0
        for i, count in enumerate(freq_values):
            # Each key can hold at most 8 letters (keys 2-9)
            # First 8 letters: 1 push, next 8: 2 pushes, etc.
            pushes += count * ((i // 8) + 1)
        
        return pushes