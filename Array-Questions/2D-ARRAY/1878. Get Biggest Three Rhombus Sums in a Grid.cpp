class Solution {
public:
    vector<int> getBiggestThree(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        set<int> sums;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                // size 0 (single cell)
                sums.insert(grid[i][j]);

                int maxSize = min({i, j, m - 1 - i, n - 1 - j});
                for (int s = 1; s <= maxSize; ++s) {
                    int sum = 0;
                    for (int dr = -s; dr <= s; ++dr) {
                        int dc = s - abs(dr);
                        sum += grid[i + dr][j + dc];
                        if (dc != 0) sum += grid[i + dr][j - dc];
                    }
                    sums.insert(sum);
                }
            }
        }

        vector<int> result;
        auto it = sums.rbegin();
        for (int cnt = 0; cnt < 3 && it != sums.rend(); ++cnt, ++it)
            result.push_back(*it);
        return result;
    }
};
