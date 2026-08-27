class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
       
        n = len(s)
        total = [0] * 26
        for ch in s:
            total[ord(ch) - 97] += 1

        # Try the latest possible position where the new string becomes greater.
        for j in range(n - 1, -1, -1):
            cnt = total[:]

            # Match target[0..j-1] exactly.
            ok = True
            for k in range(j):
                idx = ord(target[k]) - 97
                if cnt[idx] == 0:
                    ok = False
                    break
                cnt[idx] -= 1

            if not ok:
                continue

            # Try to place a character greater than target[j].
            tj = ord(target[j]) - 97
            for c in range(tj + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1

                    # Build the smallest possible suffix.
                    suffix = []
                    for x in range(26):
                        if cnt[x] > 0:
                            suffix.append(chr(x + 97) * cnt[x])

                    return target[:j] + chr(c + 97) + ''.join(suffix)

        return ""