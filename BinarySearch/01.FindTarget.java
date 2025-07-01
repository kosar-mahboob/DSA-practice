package BinarySearch;

public class FindTarget {
    public static void main(String[] args) {
        int[] nums = {1,3,6,8,9};
        int target = 8;
        int index = BinarySearch(nums,target);
        System.out.println("Index:"+ index);
    }
    static int BinarySearch(int[] nums,int target){
        int start=0;
        int end= nums.length-1;
        while (start<end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] < target)
                start = mid + 1;
            else
                end = mid - 1;
        }
        return -1;
    }
}

