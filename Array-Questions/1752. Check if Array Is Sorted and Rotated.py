
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        drop_count = 0
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drop_count += 1
        return drop_count <= 1
