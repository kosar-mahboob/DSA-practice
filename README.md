
# 📘 DSA Practice Log – Binary Search Series (Questions 1 to 6)

Welcome to my DSA learning journal 👩‍💻  
Today’s update includes a written reflection of the **first 6 questions** I solved from the Binary Search pattern series.  
I’m uploading this README to **stay consistent** and keep my GitHub active, even if I didn’t upload code today 😊

---

## ✅ Q1: First and Last Position of Element in Sorted Array


**Problem:**  
Given a sorted array and a target element, find the **first** and **last** occurrence of that element using Binary Search.

**What I Learned:**
- Binary Search can be modified to find leftmost/rightmost occurrences.
- You have to perform **two separate searches** (one for first, one for last).
- Learned about using a `result` variable while searching.

---

## ✅ Q2: Count Occurrences in Sorted Array

**Problem:**  
Count how many times a target appears in a sorted array.

**What I Learned:**
- This builds on Q1 — once we get first & last positions, count = `last - first + 1`.
- Reusing logic is powerful! 💡

---

## ✅ Q3: Rotation Count in Rotated Sorted Array

**Problem:**  
Given a rotated sorted array (like [4,5,6,1,2]), find the **number of times** it was rotated.

**What I Learned:**
- The answer is the index of the **minimum element**.
- Applied binary search to find the smallest value using modulo `%`.
- Discovered new trick: check `nums[mid] <= nums[prev] && nums[mid] <= nums[next]`.

---

## ✅ Q4: Search in Rotated Sorted Array

**Problem:**  
Find the index of a target in a rotated sorted array.

**What I Learned:**
- This was my favorite question 💖
- Used the idea of identifying which **half is sorted** (left or right) and only search there.
- Binary search doesn’t always apply to the whole array — just the sorted half!

---

## ✅ Q5: Square Root using Binary Search

**Problem:**  
Find the floor value of the square root of a number (like sqrt(10) = 3).

**What I Learned:**
- Binary search can solve math problems too!
- Had to use `long` to avoid overflow.
- Learned how to track possible answers using an `ans` variable.

---

## ✅ Q6: Floor of a Number in Sorted Array

**Problem:**  
Find the **greatest element ≤ target** (i.e., the floor of the target) in a sorted array.

**What I Learned:**
- Keep storing the answer if mid ≤ target.
- This question improved my confidence with edge cases and strict condition handling.

---

## 🌈 Reflection:

> 🧠 I’m proud of myself for completing these 6 Binary Search problems.  
> I didn’t upload code today, but I’m staying consistent by documenting what I’ve learned.  
> Every question helped build my thinking, and I can feel my **logic growing stronger** day by day.

---

## 💖 Author

**Kosar Bibi**  
💻  Developer & AI Dreamer  

💬 “No zero days. One step forward is still progress.”

---