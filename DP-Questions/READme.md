Here's a quick reference guide for recognizing which DP approach to use:

## DP Problem Pattern Recognition Guide

### 1. **Grid/Matrix DP Problems**
```
- "Paint N×3 Grid" → State tracking (two pattern types)
- Unique Paths → Classic 2D DP (dp[i][j] = dp[i-1][j] + dp[i][j-1])
- Minimum Path Sum → Grid traversal with min()
- Dungeon Game → Grid with bottom-up DP
- Robot Room Cleaner → Usually DFS/BFS
```

### 2. **String/Sequence DP Problems**
```
- Longest Common Subsequence → 2D DP table
- Edit Distance → 2D DP with min operations
- Longest Palindromic Subsequence → 2D DP, fill diagonally
- Regular Expression Matching → 2D DP with '*', '.' handling
- Word Break → 1D DP with dictionary lookup
```

### 3. **Knapsack Style (Choice DP)**
```
- 0/1 Knapsack → 2D DP (items × capacity)
- Coin Change (min coins) → 1D DP, min()
- Coin Change II (#combinations) → 1D DP, sum()
- Partition Equal Subset Sum → Subset sum variation
- Target Sum (+/-) → Usually memoization
```

### 4. **State Machine DP**
```
- Paint N×3 Grid → Two states (Type A/B)
- Best Time to Buy/Sell Stock → State: hold/cash
- House Robber → rob/don't rob states
- Paint House (3 colors) → Track min cost for each color
```

### 5. **Interval/Partition DP**
```
- Burst Balloons → dp[left][right]
- Matrix Chain Multiplication → O(n³) DP
- Palindrome Partitioning → dp[i] = min cuts
- Stone Game → dp[left][right]
```

### 6. **Bitmask DP (State Compression)**
```
- "Can I Win" → Bitmask for chosen numbers
- Shortest Path Visiting All Nodes → DP with bitmask
- Maximum Students Taking Exam → Grid with bitmask
- "Painting a Grid With Three Different Colors" → Bitmask of colors
```

### 7. **Digit DP (Counting)**
```
- Count numbers with digit constraints → DP[pos][tight][...]
- "Numbers At Most N Given Digit Set" → Digit DP
```

## Quick Decision Flowchart

**Question has:** → **Use:**
```
Grid + coloring constraints → State tracking (Paint N×3 Grid)
Grid + min/max path → 2D DP traversal
String matching/compare → 2D DP table
Choose items with capacity → Knapsack DP
Buy/sell decisions → State machine
Intervals/partitions → Interval DP
Exponential states → Bitmask DP
Counting numbers → Digit DP
```

##  Problem (1411)
**Why State Tracking DP?**
- ✅ Grid structure
- ✅ Color constraints (adjacent cells)
- ✅ Only 2 meaningful states (Type A/B patterns)
- ✅ Linear recurrence from row to row
- ❌ Not bitmask (too many rows for bitmask)
- ❌ Not knapsack (no capacity constraint)
- ❌ Not interval DP (no partitioning)

**Key Recognition:**
- "Paint N×3 grid" → Think: "What are valid row patterns?"
- Only 2 types of valid rows
- Recurrence between consecutive rows
- O(n) time, O(1) space possible

---

**Memo to remember:**
"Grid painting with adjacency constraints → Track pattern types between rows"
- n × 3 grid → 2 pattern types (Type A/B)
- Derive transitions, use DP
- Space can be optimized to O(1)
