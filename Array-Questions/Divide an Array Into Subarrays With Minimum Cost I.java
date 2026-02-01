// leetcode problem no : Divide an Array Into Subarrays With Minimum Cost I
class Solution {
    public int minimumCost(int[] nums) {
        int n = nums.length;
        
        // Find the two smallest values in nums[1..n-1]
        int firstMin = Integer.MAX_VALUE;
        int secondMin = Integer.MAX_VALUE;
        
        for (int i = 1; i < n; i++) {
            if (nums[i] < firstMin) {
                secondMin = firstMin;
                firstMin = nums[i];
            } else if (nums[i] < secondMin) {
                secondMin = nums[i];
            }
        }
        
        return nums[0] + firstMin + secondMin;
    }
}
