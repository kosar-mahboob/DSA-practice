class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        """
        Returns the count of numbers in [left, right] whose binary representation
        has a prime number of 1's.
        """
        # All possible prime counts for numbers up to 10^6 (max 20 bits)
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        ans = 0
        for num in range(left, right + 1):
            if num.bit_count() in primes:
                ans += 1
        return ans
