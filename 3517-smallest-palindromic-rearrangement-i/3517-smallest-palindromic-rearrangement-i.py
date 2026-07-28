class Solution(object):
    def smallestPalindrome(self, s):

        n = len(s)
        # Count frequency of each character
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        # Build first half
        first_half = []
        middle = ''
        for i in range(26):
            if freq[i] >= 2:
                first_half.append(chr(i + ord('a')) * (freq[i] // 2))
            if freq[i] % 2 == 1:
                middle = chr(i + ord('a'))
        
        # First half in ascending order
        first = ''.join(first_half)
        # Second half is reverse of first
        second = first[::-1]
        
        # If middle exists, place it in the center
        if middle:
            return first + middle + second
        return first + second