class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # Sum of first n odd numbers = n^2
        sum_odd = n * n
        # Sum of first n even numbers = n * (n + 1)
        sum_even = n * (n + 1)
        # GCD of n^2 and n*(n+1) = n * GCD(n, n+1) = n * 1 = n
        # Since GCD(n, n+1) = 1
        return n