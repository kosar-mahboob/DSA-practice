class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_gcd = []
        max_so_far = 0
        
        for num in nums:
            max_so_far = max(max_so_far, num)
            prefix_gcd.append(gcd(num, max_so_far))
        
        prefix_gcd.sort()
        
        total = 0
        left, right = 0, n - 1
        while left < right:
            total += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
        
        return total    