class Solution:
    def checkDivisibility(self, n: int) -> bool:
       
        original = n
        digit_sum = 0
        digit_prod = 1

        while n > 0:
            d = n % 10
            digit_sum += d
            digit_prod *= d
            n //= 10

        divisor = digit_sum + digit_prod
        return original % divisor == 0