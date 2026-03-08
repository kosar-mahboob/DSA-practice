class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        # Diagonal flipping: construct a binary string where the i-th character
        # is the opposite of the i-th character of the i-th string in nums.
        result = []
        for i in range(n):
            # Flip the bit at position i of the i-th string
            result.append('1' if nums[i][i] == '0' else '0')
        return ''.join(result)
