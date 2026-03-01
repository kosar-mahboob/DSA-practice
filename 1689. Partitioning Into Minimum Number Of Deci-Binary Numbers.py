class Solution:
    def minPartitions(self, n: str) -> int:
        # Find the maximum digit character in the string and convert to int
        return max(int(d) for d in n)
