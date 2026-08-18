class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MAX_VAL = 50
        cnt = [0] * (MAX_VAL + 1)

        # Count how many k-size windows contain each value
        for start in range(n - k + 1):
            seen = [False] * (MAX_VAL + 1)
            for i in range(start, start + k):
                v = nums[i]
                if not seen[v]:
                    seen[v] = True
                    cnt[v] += 1

        # Return largest value that appears in exactly one window
        for v in range(MAX_VAL, -1, -1):
            if cnt[v] == 1:
                return v
        return -1