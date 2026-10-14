class Solution:
    def maxSumOfSquares(self, num: int, sum_: int) -> str:
        # Impossible: digit sum too large or too small
        if sum_ > 9 * num or sum_ < 1:
            return ""
        
        # We want to maximize sum of squares of digits.
        # Squares grow faster with bigger digits, so use as many 9s as possible.
        nines = sum_ // 9
        rem = sum_ % 9
        
        digits = []
        if nines >= num:
            # All digits can be 9
            return "9" * num
        
        # We have nines full 9s, then one digit `rem`, then pad with 0s at the END
        # To maximize the number lexicographically while keeping the same score:
        # put largest digits first, smallest last.
        if rem > 0:
            digits = [9] * nines + [rem]
        else:
            digits = [9] * nines
        
        # Pad with zeros at the end to reach num length
        zeros = num - len(digits)
        digits += [0] * zeros
        

        digits.sort(reverse=True)
        
        return ''.join(map(str, digits))