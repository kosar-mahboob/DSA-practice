




# 📘 DSA Practice Log – Binary Search Series (Questions 1 to 6)

Welcome to my DSA learning journal 👩‍💻  
Today’s update includes a written reflection of the **first 6 questions** I solved from the Binary Search pattern series.  
I’m uploading this README to **stay consistent** and keep my GitHub active, even if I didn’t upload code today 😊

---

## ✅ Q1: First and Last Position of Element in Sorted Array




**Problem:**  
Given a sorted array and a target element, find the **first** and **last** occurrence of that element using Binary Search.

**What I Learned:**
- Binary Search can be modified to find leftmost/rightmost occurrences.
- You have to perform **two separate searches** (one for first, one for last).
- Learned about using a `result` variable while searching.

---

## ✅ Q2: Count Occurrences in Sorted Array

**Problem:**  
Count how many times a target appears in a sorted array.

**What I Learned:**
- This builds on Q1 — once we get first & last positions, count = `last - first + 1`.
- Reusing logic is powerful! 💡

---

## ✅ Q3: Rotation Count in Rotated Sorted Array

**Problem:**  
Given a rotated sorted array (like [4,5,6,1,2]), find the **number of times** it was rotated.

**What I Learned:**
- The answer is the index of the **minimum element**.
- Applied binary search to find the smallest value using modulo `%`.
- Discovered new trick: check `nums[mid] <= nums[prev] && nums[mid] <= nums[next]`.

---

## ✅ Q4: Search in Rotated Sorted Array

**Problem:**  
Find the index of a target in a rotated sorted array.

**What I Learned:**
- This was my favorite question 💖
- Used the idea of identifying which **half is sorted** (left or right) and only search there.
- Binary search doesn’t always apply to the whole array — just the sorted half!

---

## ✅ Q5: Square Root using Binary Search

**Problem:**  
Find the floor value of the square root of a number (like sqrt(10) = 3).

**What I Learned:**
- Binary search can solve math problems too!
- Had to use `long` to avoid overflow.
- Learned how to track possible answers using an `ans` variable.

---

## ✅ Q6: Floor of a Number in Sorted Array

**Problem:**  
Find the **greatest element ≤ target** (i.e., the floor of the target) in a sorted array.

**What I Learned:**
- Keep storing the answer if mid ≤ target.
- This question improved my confidence with edge cases and strict condition handling.

---

## 🌈 Reflection:

> 🧠 I’m proud of myself for completing these 6 Binary Search problems.  
> I didn’t upload code today, but I’m staying consistent by documenting what I’ve learned.  
> Every question helped build my thinking, and I can feel my **logic growing stronger** day by day.

---



## 💖 Author

**Kosar Bibi**  
💻  Developer & AI Dreamer  

💬 “No zero days. One step forward is still progress.”

---
<!---LeetCode Topics Start-->
# LeetCode Topics
## Two Pointers
|  |
| ------- |
| [0005-longest-palindromic-substring](https://github.com/kosar-mahboob/DSA-practice/tree/master/0005-longest-palindromic-substring) |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3534-path-existence-queries-in-a-graph-ii) |
## String
|  |
| ------- |
| [0005-longest-palindromic-substring](https://github.com/kosar-mahboob/DSA-practice/tree/master/0005-longest-palindromic-substring) |
| [1358-number-of-substrings-containing-all-three-characters](https://github.com/kosar-mahboob/DSA-practice/tree/master/1358-number-of-substrings-containing-all-three-characters) |
| [1967-number-of-strings-that-appear-as-substrings-in-word](https://github.com/kosar-mahboob/DSA-practice/tree/master/1967-number-of-strings-that-appear-as-substrings-in-word) |
| [3756-concatenate-non-zero-digits-and-multiply-by-sum-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3756-concatenate-non-zero-digits-and-multiply-by-sum-ii) |
## Dynamic Programming
|  |
| ------- |
| [0005-longest-palindromic-substring](https://github.com/kosar-mahboob/DSA-practice/tree/master/0005-longest-palindromic-substring) |
| [1301-number-of-paths-with-max-score](https://github.com/kosar-mahboob/DSA-practice/tree/master/1301-number-of-paths-with-max-score) |
| [3336-find-the-number-of-subsequences-with-equal-gcd](https://github.com/kosar-mahboob/DSA-practice/tree/master/3336-find-the-number-of-subsequences-with-equal-gcd) |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3534-path-existence-queries-in-a-graph-ii) |
| [3620-network-recovery-pathways](https://github.com/kosar-mahboob/DSA-practice/tree/master/3620-network-recovery-pathways) |
| [3700-number-of-zigzag-arrays-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3700-number-of-zigzag-arrays-ii) |
## Math
|  |
| ------- |
| [3336-find-the-number-of-subsequences-with-equal-gcd](https://github.com/kosar-mahboob/DSA-practice/tree/master/3336-find-the-number-of-subsequences-with-equal-gcd) |
| [3658-gcd-of-odd-and-even-sums](https://github.com/kosar-mahboob/DSA-practice/tree/master/3658-gcd-of-odd-and-even-sums) |
| [3700-number-of-zigzag-arrays-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3700-number-of-zigzag-arrays-ii) |
| [3754-concatenate-non-zero-digits-and-multiply-by-sum-i](https://github.com/kosar-mahboob/DSA-practice/tree/master/3754-concatenate-non-zero-digits-and-multiply-by-sum-i) |
| [3756-concatenate-non-zero-digits-and-multiply-by-sum-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3756-concatenate-non-zero-digits-and-multiply-by-sum-ii) |
## Database
|  |
| ------- |
| [1757-recyclable-and-low-fat-products](https://github.com/kosar-mahboob/DSA-practice/tree/master/1757-recyclable-and-low-fat-products) |
## Array
|  |
| ------- |
| [1288-remove-covered-intervals](https://github.com/kosar-mahboob/DSA-practice/tree/master/1288-remove-covered-intervals) |
| [1301-number-of-paths-with-max-score](https://github.com/kosar-mahboob/DSA-practice/tree/master/1301-number-of-paths-with-max-score) |
| [1331-rank-transform-of-an-array](https://github.com/kosar-mahboob/DSA-practice/tree/master/1331-rank-transform-of-an-array) |
| [1846-maximum-element-after-decreasing-and-rearranging](https://github.com/kosar-mahboob/DSA-practice/tree/master/1846-maximum-element-after-decreasing-and-rearranging) |
| [1967-number-of-strings-that-appear-as-substrings-in-word](https://github.com/kosar-mahboob/DSA-practice/tree/master/1967-number-of-strings-that-appear-as-substrings-in-word) |
| [3020-find-the-maximum-number-of-elements-in-subset](https://github.com/kosar-mahboob/DSA-practice/tree/master/3020-find-the-maximum-number-of-elements-in-subset) |
| [3286-find-a-safe-walk-through-a-grid](https://github.com/kosar-mahboob/DSA-practice/tree/master/3286-find-a-safe-walk-through-a-grid) |
| [3336-find-the-number-of-subsequences-with-equal-gcd](https://github.com/kosar-mahboob/DSA-practice/tree/master/3336-find-the-number-of-subsequences-with-equal-gcd) |
| [3532-path-existence-queries-in-a-graph-i](https://github.com/kosar-mahboob/DSA-practice/tree/master/3532-path-existence-queries-in-a-graph-i) |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3534-path-existence-queries-in-a-graph-ii) |
| [3620-network-recovery-pathways](https://github.com/kosar-mahboob/DSA-practice/tree/master/3620-network-recovery-pathways) |
| [3737-count-subarrays-with-majority-element-i](https://github.com/kosar-mahboob/DSA-practice/tree/master/3737-count-subarrays-with-majority-element-i) |
| [3739-count-subarrays-with-majority-element-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3739-count-subarrays-with-majority-element-ii) |
## Hash Table
|  |
| ------- |
| [1331-rank-transform-of-an-array](https://github.com/kosar-mahboob/DSA-practice/tree/master/1331-rank-transform-of-an-array) |
| [1358-number-of-substrings-containing-all-three-characters](https://github.com/kosar-mahboob/DSA-practice/tree/master/1358-number-of-substrings-containing-all-three-characters) |
| [3020-find-the-maximum-number-of-elements-in-subset](https://github.com/kosar-mahboob/DSA-practice/tree/master/3020-find-the-maximum-number-of-elements-in-subset) |
| [3532-path-existence-queries-in-a-graph-i](https://github.com/kosar-mahboob/DSA-practice/tree/master/3532-path-existence-queries-in-a-graph-i) |
| [3737-count-subarrays-with-majority-element-i](https://github.com/kosar-mahboob/DSA-practice/tree/master/3737-count-subarrays-with-majority-element-i) |
| [3739-count-subarrays-with-majority-element-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3739-count-subarrays-with-majority-element-ii) |
## Divide and Conquer
|  |
| ------- |
| [3737-count-subarrays-with-majority-element-i](https://github.com/kosar-mahboob/DSA-practice/tree/master/3737-count-subarrays-with-majority-element-i) |
| [3739-count-subarrays-with-majority-element-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3739-count-subarrays-with-majority-element-ii) |
## Segment Tree
|  |
| ------- |
| [3737-count-subarrays-with-majority-element-i](https://github.com/kosar-mahboob/DSA-practice/tree/master/3737-count-subarrays-with-majority-element-i) |
| [3739-count-subarrays-with-majority-element-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3739-count-subarrays-with-majority-element-ii) |
## Merge Sort
|  |
| ------- |
| [3737-count-subarrays-with-majority-element-i](https://github.com/kosar-mahboob/DSA-practice/tree/master/3737-count-subarrays-with-majority-element-i) |
| [3739-count-subarrays-with-majority-element-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3739-count-subarrays-with-majority-element-ii) |
## Counting
|  |
| ------- |
| [3737-count-subarrays-with-majority-element-i](https://github.com/kosar-mahboob/DSA-practice/tree/master/3737-count-subarrays-with-majority-element-i) |
## Prefix Sum
|  |
| ------- |
| [3737-count-subarrays-with-majority-element-i](https://github.com/kosar-mahboob/DSA-practice/tree/master/3737-count-subarrays-with-majority-element-i) |
| [3739-count-subarrays-with-majority-element-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3739-count-subarrays-with-majority-element-ii) |
| [3756-concatenate-non-zero-digits-and-multiply-by-sum-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3756-concatenate-non-zero-digits-and-multiply-by-sum-ii) |
## Enumeration
|  |
| ------- |
| [1291-sequential-digits](https://github.com/kosar-mahboob/DSA-practice/tree/master/1291-sequential-digits) |
| [3020-find-the-maximum-number-of-elements-in-subset](https://github.com/kosar-mahboob/DSA-practice/tree/master/3020-find-the-maximum-number-of-elements-in-subset) |
## Greedy
|  |
| ------- |
| [1846-maximum-element-after-decreasing-and-rearranging](https://github.com/kosar-mahboob/DSA-practice/tree/master/1846-maximum-element-after-decreasing-and-rearranging) |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3534-path-existence-queries-in-a-graph-ii) |
## Sorting
|  |
| ------- |
| [1288-remove-covered-intervals](https://github.com/kosar-mahboob/DSA-practice/tree/master/1288-remove-covered-intervals) |
| [1331-rank-transform-of-an-array](https://github.com/kosar-mahboob/DSA-practice/tree/master/1331-rank-transform-of-an-array) |
| [1846-maximum-element-after-decreasing-and-rearranging](https://github.com/kosar-mahboob/DSA-practice/tree/master/1846-maximum-element-after-decreasing-and-rearranging) |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3534-path-existence-queries-in-a-graph-ii) |
## Sliding Window
|  |
| ------- |
| [1358-number-of-substrings-containing-all-three-characters](https://github.com/kosar-mahboob/DSA-practice/tree/master/1358-number-of-substrings-containing-all-three-characters) |
## Breadth-First Search
|  |
| ------- |
| [2492-minimum-score-of-a-path-between-two-cities](https://github.com/kosar-mahboob/DSA-practice/tree/master/2492-minimum-score-of-a-path-between-two-cities) |
| [2685-count-the-number-of-complete-components](https://github.com/kosar-mahboob/DSA-practice/tree/master/2685-count-the-number-of-complete-components) |
| [3286-find-a-safe-walk-through-a-grid](https://github.com/kosar-mahboob/DSA-practice/tree/master/3286-find-a-safe-walk-through-a-grid) |
## Graph Theory
|  |
| ------- |
| [2492-minimum-score-of-a-path-between-two-cities](https://github.com/kosar-mahboob/DSA-practice/tree/master/2492-minimum-score-of-a-path-between-two-cities) |
| [2685-count-the-number-of-complete-components](https://github.com/kosar-mahboob/DSA-practice/tree/master/2685-count-the-number-of-complete-components) |
| [3286-find-a-safe-walk-through-a-grid](https://github.com/kosar-mahboob/DSA-practice/tree/master/3286-find-a-safe-walk-through-a-grid) |
| [3532-path-existence-queries-in-a-graph-i](https://github.com/kosar-mahboob/DSA-practice/tree/master/3532-path-existence-queries-in-a-graph-i) |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3534-path-existence-queries-in-a-graph-ii) |
| [3620-network-recovery-pathways](https://github.com/kosar-mahboob/DSA-practice/tree/master/3620-network-recovery-pathways) |
## Heap (Priority Queue)
|  |
| ------- |
| [3286-find-a-safe-walk-through-a-grid](https://github.com/kosar-mahboob/DSA-practice/tree/master/3286-find-a-safe-walk-through-a-grid) |
| [3620-network-recovery-pathways](https://github.com/kosar-mahboob/DSA-practice/tree/master/3620-network-recovery-pathways) |
## Matrix
|  |
| ------- |
| [1301-number-of-paths-with-max-score](https://github.com/kosar-mahboob/DSA-practice/tree/master/1301-number-of-paths-with-max-score) |
| [3286-find-a-safe-walk-through-a-grid](https://github.com/kosar-mahboob/DSA-practice/tree/master/3286-find-a-safe-walk-through-a-grid) |
## Shortest Path
|  |
| ------- |
| [3286-find-a-safe-walk-through-a-grid](https://github.com/kosar-mahboob/DSA-practice/tree/master/3286-find-a-safe-walk-through-a-grid) |
| [3620-network-recovery-pathways](https://github.com/kosar-mahboob/DSA-practice/tree/master/3620-network-recovery-pathways) |
## Binary Search
|  |
| ------- |
| [3532-path-existence-queries-in-a-graph-i](https://github.com/kosar-mahboob/DSA-practice/tree/master/3532-path-existence-queries-in-a-graph-i) |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3534-path-existence-queries-in-a-graph-ii) |
| [3620-network-recovery-pathways](https://github.com/kosar-mahboob/DSA-practice/tree/master/3620-network-recovery-pathways) |
## Topological Sort
|  |
| ------- |
| [3620-network-recovery-pathways](https://github.com/kosar-mahboob/DSA-practice/tree/master/3620-network-recovery-pathways) |
## Depth-First Search
|  |
| ------- |
| [2492-minimum-score-of-a-path-between-two-cities](https://github.com/kosar-mahboob/DSA-practice/tree/master/2492-minimum-score-of-a-path-between-two-cities) |
| [2685-count-the-number-of-complete-components](https://github.com/kosar-mahboob/DSA-practice/tree/master/2685-count-the-number-of-complete-components) |
## Union-Find
|  |
| ------- |
| [2492-minimum-score-of-a-path-between-two-cities](https://github.com/kosar-mahboob/DSA-practice/tree/master/2492-minimum-score-of-a-path-between-two-cities) |
| [2685-count-the-number-of-complete-components](https://github.com/kosar-mahboob/DSA-practice/tree/master/2685-count-the-number-of-complete-components) |
| [3532-path-existence-queries-in-a-graph-i](https://github.com/kosar-mahboob/DSA-practice/tree/master/3532-path-existence-queries-in-a-graph-i) |
## Bit Manipulation
|  |
| ------- |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/kosar-mahboob/DSA-practice/tree/master/3534-path-existence-queries-in-a-graph-ii) |
## Number Theory
|  |
| ------- |
| [3336-find-the-number-of-subsequences-with-equal-gcd](https://github.com/kosar-mahboob/DSA-practice/tree/master/3336-find-the-number-of-subsequences-with-equal-gcd) |
| [3658-gcd-of-odd-and-even-sums](https://github.com/kosar-mahboob/DSA-practice/tree/master/3658-gcd-of-odd-and-even-sums) |
<!---LeetCode Topics End-->