class Solution:
    def sumGame(self, num: str) -> bool:
      
        n = len(num)
        half = n // 2

        left_sum = right_sum = 0
        left_q = right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        total_q = left_q + right_q

        # If total '?' is odd, Alice makes the last move → she wins.
        if total_q % 2 == 1:
            return True

        diff = left_sum - right_sum
        target = (right_q - left_q) * 9 // 2

        return diff != target