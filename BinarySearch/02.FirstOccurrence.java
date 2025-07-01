// 02 - First Occurrence of Target in Sorted Array

public class FirstOccurrence {
    public static void main(String[] args) {
        int[] nums = {1, 2, 2, 2, 3, 4, 5};
        int target = 2;
        int index = firstOccurrence(nums, target);
        System.out.println("First Occurrence at index: " + index);
    }

    static int firstOccurrence(int[] arr, int target) {
        int start = 0, end = arr.length - 1;
        int result = -1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (arr[mid] == target) {
                result = mid;
                end = mid - 1; // go left for first occurrence
            } else if (arr[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return result;
    }
}
