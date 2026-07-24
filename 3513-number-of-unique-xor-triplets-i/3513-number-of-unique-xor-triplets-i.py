class Solution(object):
    def uniqueXorTriplets(self, nums):
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # For n >= 3, answer is the smallest power of 2 > n
        ans = 1
        while ans <= n:  # Need > n, not >= n
            ans <<= 1
        
        return ans