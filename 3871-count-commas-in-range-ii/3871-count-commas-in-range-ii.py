class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        d = 1
        while True:
            low = 10 ** (d - 1)
            high = 10 ** d - 1

            if low > n:
                break

            cnt = min(n, high) - low + 1
            commas_per_num = (d - 1) // 3
            ans += cnt * commas_per_num

            d += 1

        return ans