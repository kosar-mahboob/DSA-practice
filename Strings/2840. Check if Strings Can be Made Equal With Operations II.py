from collections import Counter

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # Count characters at even indices
        even1 = Counter(s1[i] for i in range(0, len(s1), 2))
        even2 = Counter(s2[i] for i in range(0, len(s2), 2))
        if even1 != even2:
            return False

        # Count characters at odd indices
        odd1 = Counter(s1[i] for i in range(1, len(s1), 2))
        odd2 = Counter(s2[i] for i in range(1, len(s2), 2))
        return odd1 == odd2
