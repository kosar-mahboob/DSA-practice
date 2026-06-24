class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        if n == 1:
            return m % MOD
        
        # We need matrix exponentiation to handle n up to 1e9
        # State vector: [up0, up1, ..., up_{m-1}, down0, down1, ..., down_{m-1}]
        # Actually up/down are related by symmetry: up_i = down_{m-1-i}
        # But we can just do matrix exponentiation on 2m states
        
        size = 2 * m
        # Build transition matrix T
        # For each v:
        # new_up[v] = sum_{w < v} down[w]
        # new_down[v] = sum_{w > v} up[w]
        
        # We'll compute (T^ (n-2)) * base_vector
        # base vector for length 2:
        # up_base[v] = v, down_base[v] = m-1-v
        
        def mat_mul(A, B):
            # A, B are size x size matrices
            result = [[0] * size for _ in range(size)]
            for i in range(size):
                Ai = A[i]
                Ri = result[i]
                for k in range(size):
                    if Ai[k]:
                        Bk = B[k]
                        val = Ai[k]
                        for j in range(size):
                            Ri[j] = (Ri[j] + val * Bk[j]) % MOD
            return result
        
        def mat_vec_mul(A, vec):
            result = [0] * size
            for i in range(size):
                total = 0
                Ai = A[i]
                for j in range(size):
                    if Ai[j] and vec[j]:
                        total = (total + Ai[j] * vec[j]) % MOD
                result[i] = total
            return result
        
        # Build transition matrix for one step (length i -> i+1)
        T = [[0] * size for _ in range(size)]
        for v in range(m):
            # new_up[v] = sum of down[w] for w < v
            for w in range(v):
                T[v][m + w] = 1
            # new_down[v] = sum of up[w] for w > v
            for w in range(v + 1, m):
                T[m + v][w] = 1
        
        # Base vector for length 2
        base = [0] * size
        for v in range(m):
            base[v] = v                     # up[v]
            base[m + v] = m - 1 - v         # down[v]
        
        # If n == 2, just return sum(base)
        if n == 2:
            return sum(base) % MOD
        
        # Need T^(n-2) * base
        # Binary exponentiation
        power = n - 2
        # Identity matrix
        result_mat = [[0] * size for _ in range(size)]
        for i in range(size):
            result_mat[i][i] = 1
        # base matrix = T
        base_mat = T
        
        while power > 0:
            if power & 1:
                result_mat = mat_mul(result_mat, base_mat)
            base_mat = mat_mul(base_mat, base_mat)
            power >>= 1
        
        final_vec = mat_vec_mul(result_mat, base)
        return sum(final_vec) % MOD