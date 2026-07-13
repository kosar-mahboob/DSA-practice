class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        # Generate all sequential digit numbers
        for start in range(1, 10):  # starting digit 1-9
            num = start
            next_digit = start + 1
            while next_digit <= 9 and num <= high:
                num = num * 10 + next_digit
                if low <= num <= high:
                    result.append(num)
                next_digit += 1
        
        return sorted(result)