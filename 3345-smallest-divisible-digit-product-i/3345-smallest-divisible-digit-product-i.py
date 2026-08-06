class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            prod, temp = 1, n
            while temp:
                prod *= temp % 10
                temp //= 10
            if prod % t == 0:
                return n
            n += 1