class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        total_k = k1 + k2
        n = len(nums1)
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]

        # Binary search on the final maximum difference we allow
        lo, hi = 0, max(diffs)
        while lo < hi:
            mid = (lo + hi) // 2
            # ops needed to bring all diffs down to <= mid
            ops = 0
            for d in diffs:
                if d > mid:
                    ops += d - mid
                    if ops > total_k:
                        break
            if ops <= total_k:
                hi = mid
            else:
                lo = mid + 1

        # Now lo = the smallest max value reachable
        # Bring all diffs down to <= lo, count total ops used
        ops_used = 0
        ans = 0
        for d in diffs:
            if d > lo:
                ops_used += d - lo
                d = lo
            ans += d * d

        # We may still have leftover ops; we can reduce some diffs equal to `lo` by 1
        leftover = total_k - ops_used
        if lo > 0 and leftover > 0:
            # count how many diffs are exactly `lo`
            cnt_at_lo = sum(1 for d in diffs if d >= lo)  # wait, careful
            # Actually: after clamping, every diff that was >= lo is now lo.
            # We can reduce some of them further by 1.
            cnt_at_lo = sum(1 for d in diffs if d >= lo)
            take = min(leftover, cnt_at_lo)
            ans -= take * (2 * lo - 1)  # d² -> (d-1)² decreases by 2d-1

        return ans