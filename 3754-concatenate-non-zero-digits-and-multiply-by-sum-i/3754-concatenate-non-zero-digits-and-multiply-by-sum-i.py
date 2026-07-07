class Solution:
    def sumAndMultiply(self, n: int) -> int:
    
        if n == 0:
            return 0
        
        # Extract digits from right to left
        digits = []
        while n > 0:
            digit = n % 10
            n //= 10
            if digit != 0:
                digits.append(digit)
        
        # Reverse to get original order
        digits.reverse()
        
        x = 0
        digit_sum = 0
        for d in digits:
            x = x * 10 + d
            digit_sum += d
        
        return x * digit_sum