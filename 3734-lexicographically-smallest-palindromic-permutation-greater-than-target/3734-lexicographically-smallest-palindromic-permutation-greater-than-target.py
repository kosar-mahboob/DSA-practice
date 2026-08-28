class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total = [0] * 26
        for ch in s:
            total[ord(ch) - 97] += 1

        # Palindrome permutation exists only if at most one odd count
        odd_chars = sum(c % 2 for c in total)
        if odd_chars > 1:
            return ""

        half_cnt = [c // 2 for c in total]
        mid = ""
        if n % 2 == 1:
            for i in range(26):
                if total[i] % 2 == 1:
                    mid = chr(i + 97)
                    break

        m = n // 2
        t_half = target[:m]

        # 1. Check if we can exactly match the target half
        if self.can_form(t_half, half_cnt):
            pal = t_half + mid + t_half[::-1]
            if pal > target:
                return pal

        # 2. Find the lexicographically smallest half > t_half
        p = self.next_greater(t_half, half_cnt)
        if p is None:
            return ""

        return p + mid + p[::-1]

    def can_form(self, t: str, cnt: list) -> bool:
        tmp = cnt[:]
        for ch in t:
            idx = ord(ch) - 97
            if tmp[idx] == 0:
                return False
            tmp[idx] -= 1
        return True

    def next_greater(self, t: str, cnt: list) -> str | None:
        n = len(t)
        for j in range(n - 1, -1, -1):
            rem = cnt[:]

            ok = True
            for k in range(j):
                idx = ord(t[k]) - 97
                if rem[idx] == 0:
                    ok = False
                    break
                rem[idx] -= 1

            if not ok:
                continue

            tj = ord(t[j]) - 97
            for c in range(tj + 1, 26):
                if rem[c] > 0:
                    rem[c] -= 1
                    suffix = []
                    for x in range(26):
                        if rem[x] > 0:
                            suffix.append(chr(x + 97) * rem[x])
                    return t[:j] + chr(c + 97) + ''.join(suffix)

        return None