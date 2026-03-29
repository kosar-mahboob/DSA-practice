class Solution {
public:
    string getHappyString(int n, int k) {
        // Total happy strings of length n = 3 * 2^(n-1)
        // because first char has 3 choices, each subsequent has 2 choices
        
        int total = 3 * (1 << (n - 1));
        if (k > total) return "";
        
        
        string result;
        // Build the string character by character
        for (int i = 0; i < n; i++) {
            // Try each possible character in lexicographical order
            for (char ch : {'a', 'b', 'c'}) {
                // Skip if same as last character
                if (!result.empty() && result.back() == ch) continue;
                
                // Calculate how many strings start with result + ch
                int remaining = n - i - 1;
                int count = 1 << remaining; // each remaining position has 2 choices
                
                if (k > count) {
                    k -= count; // skip this block
                } else {
                    result.push_back(ch);
                    break;
                }
            }
        }
        return result;
    }
};
