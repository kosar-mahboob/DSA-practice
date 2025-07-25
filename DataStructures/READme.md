# 📌 Java Array Operations

A simple Java program demonstrating basic operations on arrays like **traversal**, **insertion**, **deletion**, **searching**, **updating**, **sorting**, and **copying**. Ideal for beginners learning how to manipulate arrays manually without using ArrayLists.

---

## ✨ Features

This program includes the following array operations:

| Operation | Description |
|----------|-------------|
| **Traversal** | Print all elements of the array |
| **Insertion** | Insert a new element at a specific index |
| **Deletion** | Delete an element at a given index |
| **Searching** | Find the index of a particular value using linear search |
| **Updating** | Update the value at a given index |
| **Sorting** | Sort the array in ascending order |
| **Copying** | Create a copy of the array |

---

## 🧾 How It Works

The program uses static methods inside a class called `Array` to perform various operations on a 1D array of integers.

### Sample Workflow

```java
int[] arr = {5, 2, 8, 1, 3};

// Inserting 10 at index 2
arr = insert(arr, 2, 10);

// Deleting element at index 3
arr = delete(arr, 3);

// Searching for 8
int index = search(arr, 8);

// Updating index 1 to 20
update(arr, 1, 20);

// Sorting the array
sort(arr);

// Copying the array
int[] arrCopy = copy(arr);