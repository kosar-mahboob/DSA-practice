class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result_chars = []
        for w in words:
            total = sum(weights[ord(ch) - ord('a')] for ch in w)
            r = total % 26
            # mapping: 0 -> 'z', 1 -> 'y', ..., 25 -> 'a'
            mapped_char = chr(ord('z') - r)
            result_chars.append(mapped_char)
        return ''.join(result_chars)
