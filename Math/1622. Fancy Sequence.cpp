class Fancy {
private:
    static const int MOD = 1e9 + 7;
    vector<long long> original;   // stored values after removing global transformations
    long long mul, add;           // current transformation: value = (original * mul + add) % MOD

    long long modPow(long long a, long long e) {
        long long res = 1;
        while (e) {
            if (e & 1) res = (res * a) % MOD;
            a = (a * a) % MOD;
            e >>= 1;
        }
        return res;
    }

    long long inv(long long x) {
        return modPow(x, MOD - 2);
    }

public:
    Fancy() {
        mul = 1;
        add = 0;
    }
    
    void append(int val) {
        // current value = (x * mul + add) % MOD == val
        // => x = (val - add) * inv(mul) % MOD
        long long x = (val - add + MOD) % MOD;
        x = (x * inv(mul)) % MOD;
        original.push_back(x);
    }
    
    void addAll(int inc) {
        add = (add + inc) % MOD;
    }
    
    void multAll(int m) {
        mul = (mul * m) % MOD;
        add = (add * m) % MOD;
    }
    
    int getIndex(int idx) {
        if (idx >= (int)original.size()) return -1;
        long long res = (original[idx] * mul + add) % MOD;
        return (int)res;
    }
};
