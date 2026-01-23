//leetcodeproblem no : 3510 Minimum Pair Removal to Sort Array II

class Solution {
    using ll = long long;
public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size(); 
        vector<ll> value(n);
        vector<int> prevInd(n), nextInd(n); // -1 mean non-valid
        priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> minHeap;
        int reverseNum = 0;
        // 1. start to initialization
        iota(prevInd.begin(), prevInd.end(), -1);
        iota(nextInd.begin(), nextInd.end(), 1);
        nextInd.back() = -1;
        for(int i=0; i<n; ++i){
            value[i] = nums[i];
            if(i!=n-1){
                if(nums[i] > nums[i+1]) reverseNum++;
                minHeap.push({nums[i] + nums[i+1], i});
            } 
        }

        // 2. Run each operation O(log n)
        int count = 0;
        while(reverseNum > 0){
            auto [nodeVal, pos] = minHeap.top();
            minHeap.pop();
            // 2-a. check if valid, invalid when next, prev are both -1.
            if(nextInd[pos] == -1 || nodeVal != value[pos] + value[nextInd[pos]]) continue;

            // 2-b. update prevInd, nextInd -> minus reverseNum -> value -> (add reverseNum + minHeap)
            int pos2 = nextInd[pos];
            nextInd[pos] = nextInd[pos2];
            if(nextInd[pos] != -1) prevInd[nextInd[pos]] = pos;
            nextInd[pos2] = prevInd[pos2] = -1;

            if(prevInd[pos] != -1 && value[prevInd[pos]] > value[pos]) --reverseNum;
            if(value[pos] > value[pos2]) --reverseNum;
            if(nextInd[pos] != -1 && value[pos2] > value[nextInd[pos]]) --reverseNum;

            value[pos] += value[pos2];

            if(prevInd[pos] != -1){
                if(value[prevInd[pos]] > value[pos]) ++reverseNum;
                minHeap.push({value[pos] + value[prevInd[pos]], prevInd[pos]});
            }
            if(nextInd[pos] != -1){
                if(value[pos] > value[nextInd[pos]]) ++reverseNum;
                minHeap.push({value[pos] + value[nextInd[pos]], pos});
            }
            ++count;
        }
        return count;
    }
};
