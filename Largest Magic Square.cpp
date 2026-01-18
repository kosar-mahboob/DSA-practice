class Solution {
public:
    int largestMagicSquare(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> rowPrefix(m+1, vector<int>(n+1, 0));
        vector<vector<int>> colPrefix(m+1, vector<int>(n+1, 0));
        
        // Build prefix sums for rows and columns
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                rowPrefix[i+1][j+1] = rowPrefix[i+1][j] + grid[i][j];
                colPrefix[i+1][j+1] = colPrefix[i][j+1] + grid[i][j];
            }
        }
        
        // Helper to get row sum from (r, c1) to (r, c2) inclusive
        auto rowSum = [&](int r, int c1, int c2) {
            return rowPrefix[r+1][c2+1] - rowPrefix[r+1][c1];
        };
        
        // Helper to get column sum from (r1, c) to (r2, c) inclusive
        auto colSum = [&](int r1, int c, int r2) {
            return colPrefix[r2+1][c+1] - colPrefix[r1][c+1];
        };
        
        // Check all possible squares from largest k to smallest
        for (int k = min(m, n); k > 1; k--) {
            for (int i = 0; i + k <= m; i++) {
                for (int j = 0; j + k <= n; j++) {
                    // Check if square with top-left (i, j) and size k is magic
                    int sum = rowSum(i, j, j+k-1); // first row sum as reference
                    bool valid = true;
                    
                    // Check rows
                    for (int r = i+1; r < i+k; r++) {
                        if (rowSum(r, j, j+k-1) != sum) {
                            valid = false;
                            break;
                        }
                    }
                    if (!valid) continue;
                    
                    // Check columns
                    for (int c = j; c < j+k; c++) {
                        if (colSum(i, c, i+k-1) != sum) {
                            valid = false;
                            break;
                        }
                    }
                    if (!valid) continue;
                    
                    // Check main diagonal
                    int diag1 = 0;
                    for (int d = 0; d < k; d++) {
                        diag1 += grid[i+d][j+d];
                    }
                    if (diag1 != sum) continue;
                    
                    // Check anti-diagonal
                    int diag2 = 0;
                    for (int d = 0; d < k; d++) {
                        diag2 += grid[i+d][j+k-1-d];
                    }
                    if (diag2 != sum) continue;
                    
                    // All checks passed
                    return k;
                }
            }
        }
        
        // If no larger magic square found, k=1 is always true
        return 1;
    }
};
