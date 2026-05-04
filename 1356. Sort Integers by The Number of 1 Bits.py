class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        """
        Sorts the array by the number of 1 bits in the binary representation,
        then by the integer value.
        """
        # Use a tuple key: (bit_count, value)
        arr.sort(key=lambda x: (x.bit_count(), x))
        return arr
        
