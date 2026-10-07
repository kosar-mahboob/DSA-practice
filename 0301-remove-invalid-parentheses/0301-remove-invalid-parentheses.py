from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Step 1: find number of misplaced '(' and ')'
        left_remove = right_remove = 0
        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        res = set()

        def dfs(i, left_count, right_count, left_rem, right_rem, path):
            if i == len(s):
                if left_rem == 0 and right_rem == 0:
                    res.add(path)
                return

            ch = s[i]

            if ch == '(':
                # Option 1: remove it
                if left_rem > 0:
                    dfs(i + 1, left_count, right_count, left_rem - 1, right_rem, path)
                # Option 2: keep it
                dfs(i + 1, left_count + 1, right_count, left_rem, right_rem, path + ch)

            elif ch == ')':
                # Option 1: remove it
                if right_rem > 0:
                    dfs(i + 1, left_count, right_count, left_rem, right_rem - 1, path)
                # Option 2: keep it if valid
                if left_count > right_count:
                    dfs(i + 1, left_count, right_count + 1, left_rem, right_rem, path + ch)

            else:
                dfs(i + 1, left_count, right_count, left_rem, right_rem, path + ch)

        dfs(0, 0, 0, left_remove, right_remove, "")
        return list(res)