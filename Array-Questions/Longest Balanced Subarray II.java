//leetcode problem no : 3721 Longest Balanced Subarray II
import java.util.*;

class Solution {
    public int longestBalanced(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;

        int maxVal = 0;
        for (int x : nums) maxVal = Math.max(maxVal, x);
        int[] last = new int[maxVal + 1];
        Arrays.fill(last, -1);

        SegTree seg = new SegTree(n);
        int ans = 0;

        for (int i = 0; i < n; i++) {
            int x = nums[i];
            int p = last[x];
            int delta = (x % 2 == 0) ? 1 : -1;
            seg.add(p + 1, i, delta);
            last[x] = i;

            int l = seg.queryLeftmostZeroPrefix(i);
            if (l != -1) {
                ans = Math.max(ans, i - l + 1);
            }
        }
        return ans;
    }

    // Segment tree supporting range add and leftmost zero query in prefix [0,i]
    static class SegTree {
        int n;
        int[] min, max, lazy;

        SegTree(int n) {
            this.n = n;
            min = new int[4 * n];
            max = new int[4 * n];
            lazy = new int[4 * n];
        }

        private void push(int idx) {
            if (lazy[idx] != 0) {
                int val = lazy[idx];
                int left = idx * 2;
                int right = idx * 2 + 1;
                min[left] += val;
                max[left] += val;
                lazy[left] += val;
                min[right] += val;
                max[right] += val;
                lazy[right] += val;
                lazy[idx] = 0;
            }
        }

        // range add [ql, qr] inclusive
        private void add(int idx, int l, int r, int ql, int qr, int val) {
            if (ql <= l && r <= qr) {
                min[idx] += val;
                max[idx] += val;
                lazy[idx] += val;
                return;
            }
            push(idx);
            int mid = (l + r) >> 1;
            if (ql <= mid) add(idx * 2, l, mid, ql, qr, val);
            if (qr > mid) add(idx * 2 + 1, mid + 1, r, ql, qr, val);
            min[idx] = Math.min(min[idx * 2], min[idx * 2 + 1]);
            max[idx] = Math.max(max[idx * 2], max[idx * 2 + 1]);
        }

        public void add(int ql, int qr, int val) {
            if (ql > qr) return;
            add(1, 0, n - 1, ql, qr, val);
        }

        // find leftmost index in [0, i] with value 0, or -1 if none
        private int queryPrefix(int idx, int l, int r, int i) {
            if (l > i || min[idx] > 0 || max[idx] < 0) return -1;
            if (l == r) return l;
            push(idx);
            int mid = (l + r) >> 1;
            if (i <= mid) {
                return queryPrefix(idx * 2, l, mid, i);
            } else {
                int leftRes = queryPrefix(idx * 2, l, mid, i);
                if (leftRes != -1) return leftRes;
                return queryPrefix(idx * 2 + 1, mid + 1, r, i);
            }
        }

        public int queryLeftmostZeroPrefix(int i) {
            return queryPrefix(1, 0, n - 1, i);
        }
    }
}
