// leetcode pronlem no : 2975 Maximum Square Area by Removing Fences From a Field
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int maximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {
        final int MOD = 1_000_000_007;
        
        // Since m, n can be up to 10^9, we can't use boolean array directly
        // But number of positions is limited to ~602
        
        // Add all row positions
        Set<Integer> rowPositions = new HashSet<>();
        rowPositions.add(1);
        rowPositions.add(m);
        for (int fence : hFences) {
            rowPositions.add(fence);
        }
        
        // Add all column positions
        Set<Integer> colPositions = new HashSet<>();
        colPositions.add(1);
        colPositions.add(n);
        for (int fence : vFences) {
            colPositions.add(fence);
        }
        
        // Convert to arrays
        Integer[] rows = rowPositions.toArray(new Integer[0]);
        Integer[] cols = colPositions.toArray(new Integer[0]);
        
        // Find maximum common gap
        int maxGap = -1;
        
        // For each possible gap in rows, check if it exists in columns
        Set<Integer> colGaps = new HashSet<>();
        for (int i = 0; i < cols.length; i++) {
            for (int j = i + 1; j < cols.length; j++) {
                colGaps.add(Math.abs(cols[i] - cols[j]));
            }
        }
        
        // Check row gaps against column gaps
        for (int i = 0; i < rows.length; i++) {
            for (int j = i + 1; j < rows.length; j++) {
                int gap = Math.abs(rows[i] - rows[j]);
                if (colGaps.contains(gap)) {
                    maxGap = Math.max(maxGap, gap);
                }
            }
        }
        
        if (maxGap == -1) return -1;
        
        long side = maxGap % MOD;
        return (int)((side * side) % MOD);
    }
}
