class Array {
    // Traversal
    static void traverse(int[] arr) {
        System.out.print("Array elements: ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }



    // Insertion (at index)
    static int[] insert(int[] arr, int index, int value) {
        if (index < 0 || index > arr.length) {
            System.out.println("Invalid index for insertion.");
            return arr;
        }
        int[] newArr = new int[arr.length + 1];
        for (int i = 0, j = 0; i < newArr.length; i++) {
            if (i == index) {
                newArr[i] = value;
            } else {
                newArr[i] = arr[j++];
            }
        }
        return newArr;
    }

    // Deletion (at index)
    static int[] delete(int[] arr, int index) {
        if (index < 0 || index >= arr.length) {
            System.out.println("Invalid index for deletion.");
            return arr;
        }
        int[] newArr = new int[arr.length - 1];
        for (int i = 0, j = 0; i < arr.length; i++) {
            if (i != index) {
                newArr[j++] = arr[i];
            }
        }
        return newArr;
    }


    // Searching (linear search)
    static int search(int[] arr, int value) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == value) return i;
        }
        return -1;
    }

    // Updating (at index)
    static void update(int[] arr, int index, int value) {
        if (index >= 0 && index < arr.length) {
            arr[index] = value;
        }
    }

    // Sorting (ascending)
    static void sort(int[] arr) {
        java.util.Arrays.sort(arr);
    }

    // Copying
    static int[] copy(int[] arr) {
        return java.util.Arrays.copyOf(arr, arr.length);
    }

    public static void main(String[] args) {
        int[] arr = {5, 2, 8, 1, 3};
        System.out.println("Original:");
        traverse(arr);

        // Insert 10 at index 2
        arr = insert(arr, 2, 10);
        System.out.println("After insertion (10 at index 2):");
        traverse(arr);

        // Delete element at index 3
        arr = delete(arr, 3);
        System.out.println("After deletion (index 3):");
        traverse(arr);

        // Search for value 8
        int idx = search(arr, 8);
        System.out.println("Index of 8: " + idx);

        // Update value at index 1 to 20
        update(arr, 1, 20);
        System.out.println("After updating index 1 to 20:");
        traverse(arr);

        // Sort array
        sort(arr);
        System.out.println("After sorting:");
        traverse(arr);

        // Copy array
        int[] arrCopy = copy(arr);
        System.out.println("Copied array:");
        traverse(arrCopy);

        // Length
        System.out.println("Array length: " + arr.length);
    }
}
