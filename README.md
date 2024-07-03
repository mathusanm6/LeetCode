# Leetcode

[![Python CI (conda)](https://github.com/mathusanMe/LeetCode/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/mathusanMe/LeetCode/actions/workflows/python-package-conda.yml)

## Description

This repository contains my solutions to LeetCode problems. I will be updating this repository with my solutions as I solve more problems. I have included a test suite for each solution.

The test suite can be run using the following command in **the repository directory**:

```bash
pytest
```

## Algorithms

- [Arrays & Hashing](https://github.com/mathusanMe/LeetCode#Arrays--Hashing)
- [Two Pointers](https://github.com/mathusanMe/LeetCode#Two-Pointers)
- [Sliding Window](https://github.com/mathusanMe/LeetCode#Sliding-Window)
- [Matrix](https://github.com/mathusanMe/LeetCode#Matrix)
- [Intervals](https://github.com/mathusanMe/LeetCode#Intervals)
- [Stack](https://github.com/mathusanMe/LeetCode#Stack)
- [Linked List](https://github.com/mathusanMe/LeetCode#Linked-List)
- [Binary Tree General](https://github.com/mathusanMe/LeetCode#Binary-Tree-General)
- [Binary Search Tree](https://github.com/mathusanMe/LeetCode#Binary-Search-Tree)
- [Graph General](https://github.com/mathusanMe/LeetCode#Graph-General)

## Arrays & Hashing

| #   | Title                                                                             | Solution                                                                                                                 | Time           | Space            | Difficulty | Tag | Note                                                                                      |
| --- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------- | ---------------- | ---------- | --- | ----------------------------------------------------------------------------------------- |
| 1   | [Two Sum](https://leetcode.com/problems/two-sum/)                                 | [Python](./problems/easy/two_sum.py)                                                                                     | _O(n)_         | _O(n)_           | Easy       |     |                                                                                           |
| 42  | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)         | [Python _O(n)_](./problems/hard/trapping_rain_water_o_n.py), [Python _O(1)_](./problems/hard/trapping_rain_water_o_1.py) | _O(n)_         | _O(n)_ or _O(1)_ | Hard       |     | Initially proposed an O(n) space complexity solution, but discovered an O(1) alternative. |
| 49  | [Group Anagrams](https://leetcode.com/problems/group-anagrams/)                   | [Python](./problems/medium/group_anagrams.py)                                                                            | _O(NK)_        | _O(NK)_          | Medium     |     | _N_ is the number of strings and _K_ is the maximum length of a single string             |
| 88  | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)           | [Python](./problems/easy/merge_sorted_array.py)                                                                          | _O(n + m)_     | _O(1)_           | Easy       |     | Two-Pointers, Reverse                                                                     |
| 135 | [Candy](https://leetcode.com/problems/candy/)                                     | [Python](./problems/hard/candy.py)                                                                                       | _O(n)_         | _O(n)_           | Hard       |     | Enjoyed solving it!                                                                       |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)           | [Python](./problems/easy/contains_duplicate.py)                                                                          | _O(n)_         | _O(n)_           | Easy       |     |                                                                                           |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/)                     | [Python](./problems/easy/valid_anagram.py)                                                                               | _O(n)_         | _O(n)_           | Easy       |     | Given Unicode characters support for Python3, the follow-up question is irrelevant        |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | [Python](./problems/medium/top_k_frequent_elements.py)                                                                   | _O(N\*log(K))_ | _O(N + K)_       | Medium     |     | Requires MinHeap                                                                          |
| 383 | [Ransom Note](https://leetcode.com/problems/ransom-note/)                         | [Python](./problems/easy/ransom_note.py)                                                                                 | _O(n)_         | _O(1)_           | Easy       |     | Fixed List                                                                                |

## Two-Pointers

| #   | Title                                                               | Solution                                      | Time   | Space  | Difficulty | Tag | Note |
| --- | ------------------------------------------------------------------- | --------------------------------------------- | ------ | ------ | ---------- | --- | ---- |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | [Python](./problems/easy/valid_palindrome.py) | _O(n)_ | _O(1)_ | Easy       |     |      |

## Sliding-Window

| #   | Title                                                                                 | Solution                                                 | Time   | Space  | Difficulty | Tag | Note |
| --- | ------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------ | ------ | ---------- | --- | ---- |
| 209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | [Python](./problems/medium/minimum_size_subarray_sum.py) | _O(n)_ | _O(1)_ | Medium     |     |      |

## Matrix

| #   | Title                                                       | Solution                                    | Time   | Space  | Difficulty | Tag | Note |
| --- | ----------------------------------------------------------- | ------------------------------------------- | ------ | ------ | ---------- | --- | ---- |
| 36  | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | [Python](./problems/medium/valid_sudoku.py) | _O(1)_ | _O(1)_ | Medium     |     |      |

## Intervals

| #   | Title                                                           | Solution                                    | Time   | Space  | Difficulty | Tag | Note |
| --- | --------------------------------------------------------------- | ------------------------------------------- | ------ | ------ | ---------- | --- | ---- |
| 228 | [Summary Ranges](https://leetcode.com/problems/summary-ranges/) | [Python](./problems/easy/summary_ranges.py) | _O(n)_ | _O(n)_ | Easy       |     |      |

## Stack

| #   | Title                                                                 | Solution                                       | Time   | Space  | Difficulty | Tag | Note |
| --- | --------------------------------------------------------------------- | ---------------------------------------------- | ------ | ------ | ---------- | --- | ---- |
| 20  | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [Python](./problems/easy/valid_parentheses.py) | _O(n)_ | _O(n)_ | Easy       |     |      |

## Linked-List

| #   | Title                                                                 | Solution                                       | Time   | Space  | Difficulty | Tag | Note |
| --- | --------------------------------------------------------------------- | ---------------------------------------------- | ------ | ------ | ---------- | --- | ---- |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | [Python](./problems/easy/linked_list_cycle.py) | _O(n)_ | _O(1)_ | Easy       |     |      |

## Binary-Tree-General

| #   | Title                                                                                       | Solution                                                   | Time   | Space  | Difficulty | Tag | Note             |
| --- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ------ | ------ | ---------- | --- | ---------------- |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Python](./problems/easy//maximum_depth_of_binary_tree.py) | _O(n)_ | _O(1)_ | Easy       | DFS | Use FIFO for BFS |

## Binary-Tree-BFS

| #   | Title                                                                                     | Solution                                                   | Time   | Space                                                  | Difficulty | Tag | Note |
| --- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ------ | ------------------------------------------------------ | ---------- | --- | ---- |
| 199 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | [Python](./problems/medium/binary_tree_right_side_view.py) | _O(n)_ | _O(w)_ where w is the maximum width of the binary tree | Medium     |     |      |

## Binary-Search-Tree

| #   | Title                                                                                                   | Solution                                                        | Time   | Space  | Difficulty | Tag | Note               |
| --- | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ------ | ------ | ---------- | --- | ------------------ |
| 530 | [Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/) | [Python](./problems/easy/minimum_absolute_difference_in_bst.py) | _O(n)_ | _O(1)_ | Easy       |     | In-order traversal |

## Graph-General

| #   | Title                                                                 | Solution                                         | Time        | Space  | Difficulty | Tag | Note |
| --- | --------------------------------------------------------------------- | ------------------------------------------------ | ----------- | ------ | ---------- | --- | ---- |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | [Python](./problems/medium/number_of_islands.py) | _O(n \* m)_ | _O(1)_ | Medium     |     |      |
