class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        
        # dp[i][j] = (max_sum, ways) from (0,0) to (i,j)
        dp = [[(-1, 0)] * n for _ in range(n)]
        dp[0][0] = (0, 1)  # start at 'E'
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X':
                    continue
                if i == 0 and j == 0:
                    continue
                
                best_sum = -1
                ways = 0
                
                # Check three possible previous cells: up, left, up-left
                for di, dj in [(-1, 0), (0, -1), (-1, -1)]:
                    pi, pj = i + di, j + dj
                    if 0 <= pi < n and 0 <= pj < n and dp[pi][pj][1] > 0:
                        s, w = dp[pi][pj]
                        # Add value of current cell if it's a number
                        if board[i][j] not in 'SE':
                            s += int(board[i][j])
                        if s > best_sum:
                            best_sum = s
                            ways = w
                        elif s == best_sum:
                            ways = (ways + w) % MOD
                
                dp[i][j] = (best_sum, ways)
        
        # Result from bottom-right 'S'
        if dp[n-1][n-1][1] == 0:
            return [0, 0]
        return [dp[n-1][n-1][0], dp[n-1][n-1][1] % MOD]