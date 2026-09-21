class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        dp = [0] * k  # counts of subarrays ending at previous index with each remainder

        for num in nums:
            r = num % k
            new_dp = [0] * k

            # start a new subarray with just this element
            new_dp[r] += 1

            # extend all previous subarrays
            for rem in range(k):
                if dp[rem]:
                    new_rem = (rem * r) % k
                    new_dp[new_rem] += dp[rem]

            # add counts to result
            for rem in range(k):
                res[rem] += new_dp[rem]

            dp = new_dp

        return res