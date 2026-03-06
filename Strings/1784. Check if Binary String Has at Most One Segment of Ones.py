class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # If there is a "01" substring, it means zeros appear between ones
        return "01" not in s
