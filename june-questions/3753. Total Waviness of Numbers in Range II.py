class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # Digit DP: returns total waviness sum for numbers in [0, N]
        def solve(N: int) -> int:
            if N < 100:
                return 0
            s = str(N)
            n = len(s)
            from functools import lru_cache

            @lru_cache(maxsize=None)
            def dp(pos: int, prev: int, prev2: int, tight: bool, started: bool):
                """
                Returns (count, total_waviness) for suffix starting at pos.
                prev: last digit placed (0-9) or -1 if none.
                prev2: second last digit placed (0-9) or -1 if none.
                """
                if pos == n:
                    # one valid number (including 0 when started=False)
                    return (1, 0)
                limit = int(s[pos]) if tight else 9
                total_cnt = 0
                total_wav = 0
                for d in range(0, limit + 1):
                    new_tight = tight and (d == limit)
                    if not started and d == 0:
                        # still leading zeros, number not started yet
                        cnt, wav = dp(pos + 1, -1, -1, new_tight, False)
                        total_cnt += cnt
                        total_wav += wav
                    else:
                        # we have started the number
                        new_started = True
                        if not started:
                            # first digit
                            new_prev = d
                            new_prev2 = -1
                            add = 0
                        else:
                            new_prev2 = prev
                            new_prev = d
                            # check if the triple (prev2, prev, d) forms a peak/valley
                            if prev2 != -1:
                                if (prev > prev2 and prev > d) or (prev < prev2 and prev < d):
                                    add = 1
                                else:
                                    add = 0
                            else:
                                add = 0
                        cnt, wav = dp(pos + 1, new_prev, new_prev2, new_tight, new_started)
                        total_cnt += cnt
                        total_wav += wav + add * cnt
                return (total_cnt, total_wav)

            # dp returns (count, total_waviness)
            return dp(0, -1, -1, True, False)[1]

        return solve(num2) - solve(num1 - 1)
