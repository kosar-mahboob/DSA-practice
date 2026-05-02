class Solution:
    def rotatedDigits(self, n: int) -> int:
        # Valid digits that remain digits after 180° rotation
        must_change = {'2', '5', '6', '9'}
        valid = {'0', '1', '8'} | must_change
        
        def is_good(num: int) -> bool:
            s = str(num)
            if any(ch not in valid for ch in s):
                return False
            # Must contain at least one digit that changes
            return any(ch in must_change for ch in s)
        
        return sum(is_good(i) for i in range(1, n + 1))
