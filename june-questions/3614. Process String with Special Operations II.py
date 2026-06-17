class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        ops = []          # list of (type, value)
        lengths = []      # length after each operation
        cur_len = 0
        
        for ch in s:
            if ch.islower():
                ops.append(('append', ch))
                cur_len += 1
            elif ch == '*':
                ops.append(('pop', None))
                if cur_len > 0:
                    cur_len -= 1
            elif ch == '#':
                ops.append(('dup', None))
                cur_len *= 2
            else:  # '%'
                ops.append(('rev', None))
                # length unchanged
            lengths.append(cur_len)
        
        # If k is out of bounds or final string empty
        if k >= lengths[-1]:
            return '.'
        
        pos = k
        for i in range(n - 1, -1, -1):
            op = ops[i]
            len_before = lengths[i - 1] if i > 0 else 0
            len_after = lengths[i]
            
            if op[0] == 'append':
                if pos == len_before:
                    return op[1]
                # otherwise pos stays the same
            elif op[0] == 'pop':
                # len_after = len_before - 1 if popped, else same
                # pos stays the same (it's valid because pos < len_after)
                pass
            elif op[0] == 'dup':
                # len_after = len_before * 2
                if pos >= len_before:
                    pos -= len_before
            else:  # 'rev'
                pos = len_before - 1 - pos
        
        return '.'  # should never reach here if k is valid
