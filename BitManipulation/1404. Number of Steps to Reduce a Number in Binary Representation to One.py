class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        while s != "1":
            if s[-1] == '0':
                # even: divide by 2 (remove last bit)
                s = s[:-1]
            else:
                # odd: add 1
                i = len(s) - 1
                # find the first '0' from the right
                while i >= 0 and s[i] == '1':
                    i -= 1
                if i >= 0:
                    # change that '0' to '1' and set following bits to '0'
                    s = s[:i] + '1' + '0' * (len(s) - i - 1)
                else:
                    # all bits are '1', so result is '1' followed by zeros
                    s = '1' + '0' * len(s)
            steps += 1
        return steps
