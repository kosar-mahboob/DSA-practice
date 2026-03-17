class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<int> heights(n, 0);
        int ans = 0;

        for (int i = 0; i < m; ++i) {
            // Update heights for current row
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == 1)
                    heights[j]++;
                else
                    heights[j] = 0;
            }

            // Sort heights descending
            vector<int> sorted = heights;
            sort(sorted.rbegin(), sorted.rend());

            // Compute max area with bottom at row i
            for (int k = 0; k < n; ++k) {
                ans = max(ans, sorted[k] * (k + 1));
            }
        }
        return ans;
    }
};
