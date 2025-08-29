# Leetcode

[![Code Health (C++)](https://github.com/mathusanm6/LeetCode/actions/workflows/postsubmit-cpp.yml/badge.svg)](https://github.com/mathusanm6/LeetCode/actions/workflows/postsubmit-cpp.yml)
[![C++ Linter](https://github.com/mathusanm6/LeetCode/actions/workflows/linter-cpp.yml/badge.svg)](https://github.com/mathusanm6/LeetCode/actions/workflows/linter-cpp.yml)

[![Code Health (Python)](https://github.com/mathusanm6/LeetCode/actions/workflows/postsubmit-py.yml/badge.svg)](https://github.com/mathusanm6/LeetCode/actions/workflows/postsubmit-py.yml)
[![Python Linter](https://github.com/mathusanm6/LeetCode/actions/workflows/linter-py.yml/badge.svg)](https://github.com/mathusanm6/LeetCode/actions/workflows/linter-py.yml)

## Description

This repository contains my solutions to LeetCode problems. I will be updating this repository with my solutions as I solve more problems. I have included a test suite for each solution.

## Running Tests

### Python Tests

To run the Python test suite, use the following commands in **the repository directory**:

```bash
# Run all Python tests
make test-py:all

# Run tests for a specific problem (e.g., two-sum)
make test-py:two-sum
```

### C++ Tests

To run the C++ test suite, use the following commands in the repository directory:

```bash
# Run all C++ tests
make test-cpp:all

# Run tests for a specific problem (e.g., two-sum)
make test-cpp:two-sum

# Run both C++ and Python tests for all problems
make test:all
```

## Code Quality

This project includes comprehensive code quality tools and automated linting:

### Linting and Formatting

```bash
# Format all code (C++ and Python)
make format

# Lint all code (C++ and Python)
make lint

# Format/lint specific languages
make format-cpp     # Format C++ files with clang-format
make format-python  # Format Python files with ruff
make lint-cpp       # Lint C++ files with clang-tidy
make lint-python    # Lint Python files with ruff
```

### Continuous Integration

- **Linters**: Automated code formatting and linting checks on every push/PR
- **Presubmit**: Comprehensive testing of changed files before merge
- **Postsubmit**: Full test suite execution after merge to main branch
- All workflows leverage the project's Makefile for consistency

## Algorithms

- [Arrays & Hashing](#arrays--hashing)
- [Two Pointers](#two-pointers)
- [Sliding Window](#sliding-window)
- [Stack](#stack)
- [Matrix](#matrix)
- [Intervals](#intervals)
- [Linked List](#linked-list)
- [Binary Tree General](#binary-tree-general)
- [Binary Search Tree](#binary-search-tree)
- [Graph General](#graph-general)

## Arrays & Hashing

| #   | Title                                                                                       | Solution                                                                                    | Time           | Space      | Difficulty | Tag | Note                                                                               |
| --- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | -------------- | ---------- | ---------- | --- | ---------------------------------------------------------------------------------- |
| 1   | [Two Sum](https://leetcode.com/problems/two-sum/)                                           | [Python](./python/problems/easy/two_sum.py), [C++](./cpp/problems/easy/two_sum/two_sum.cpp) | _O(n)_         | _O(n)_     | Easy       |     |                                                                                    |
| 49  | [Group Anagrams](https://leetcode.com/problems/group-anagrams/)                             | [Python](./python/problems/medium/group_anagrams.py)                                        | _O(NK)_        | _O(NK)_    | Medium     |     | _N_ is the number of strings and _K_ is the maximum length of a single string      |
| 88  | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)                     | [Python](./python/problems/easy/merge_sorted_array.py)                                      | _O(n + m)_     | _O(1)_     | Easy       |     | Two-Pointers, Reverse                                                              |
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | [Python](./python/problems/medium/longest_consecutive_sequence.py)                          | _O(n)_         | _O(n)_     | Medium     |     | Tricky solution!                                                                   |
| 135 | [Candy](https://leetcode.com/problems/candy/)                                               | [Python](./python/problems/hard/candy.py)                                                   | _O(n)_         | _O(n)_     | Hard       |     | Enjoyed solving it!                                                                |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)                     | [Python](./python/problems/easy/contains_duplicate.py)                                      | _O(n)_         | _O(n)_     | Easy       |     |                                                                                    |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | [Python](./python/problems/medium/product_of_array_except_self.py)                          | _O(n)_         | _O(1)_     | Medium     |     | Interesting solution!                                                              |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/)                               | [Python](./python/problems/easy/valid_anagram.py)                                           | _O(n)_         | _O(n)_     | Easy       |     | Given Unicode characters support for Python3, the follow-up question is irrelevant |
| 271 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)       | [Python](./python/problems/medium/encode_and_decode_strings.py)                             | _O(n)_         | _O(n)_     | Medium     |     |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)           | [Python](./python/problems/medium/top_k_frequent_elements.py)                               | _O(N\*log(K))_ | _O(N + K)_ | Medium     |     | Requires MinHeap                                                                   |
| 383 | [Ransom Note](https://leetcode.com/problems/ransom-note/)                                   | [Python](./python/problems/easy/ransom_note.py)                                             | _O(n)_         | _O(1)_     | Easy       |     | Fixed List                                                                         |

## Two-Pointers

| #   | Title                                                                                                 | Solution                                                                                                                               | Time     | Space            | Difficulty | Tag | Note                                                                                      |
| --- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------------- | ---------- | --- | ----------------------------------------------------------------------------------------- |
| 11  | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)                 | [Python](./python/problems/medium/container_with_most_water.py)                                                                        | _O(n)_   | _O(1)_           | Medium     |     |                                                                                           |
| 15  | [3Sum](https://leetcode.com/problems/3sum/)                                                           | [Python](./python/problems/medium/three_sum.py)                                                                                        | _O(n^2)_ | _O(1)_           | Medium     |     |                                                                                           |
| 42  | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)                             | [Python _O(n)_](./python/problems/hard/trapping_rain_water_o_n.py), [Python _O(1)_](./python/problems/hard/trapping_rain_water_o_1.py) | _O(n)_   | _O(n)_ or _O(1)_ | Hard       |     | Initially proposed an O(n) space complexity solution, but discovered an O(1) alternative. |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)                                   | [Python](./python/problems/easy/valid_palindrome.py)                                                                                   | _O(n)_   | _O(1)_           | Easy       |     |                                                                                           |
| 167 | [Two Sum II - Input Array is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Python](./python/problems/medium/two_sum_ii_input_array_is_sorted.py)                                                                 | _O(n)_   | _O(1)_           | Medium     |     |                                                                                           |

## Sliding-Window

| #   | Title                                                                                                                           | Solution                                                                             | Time                                                      | Space                                                                               | Difficulty | Tag | Note                                                                         |
| --- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------- | --- | ---------------------------------------------------------------------------- |
| 3   | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Python](./python/problems/medium/longest_substring_without_repeating_characters.py) | _O(n)_                                                    | _O(min(n, m))_, _n_ being size of the string and _m_ being the size of the alphabet | Medium     |     | A better solution would be to jump to the point where we have a valid string |
| 76  | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)                                             | [Python](./python/problems/hard/minimum_window_substring.py)                         | _O(m + n)_, _m_ being size of `s` and _n_ the size of `t` | _O(l)_, _l_ being the number of unique characters in `t`                            | Hard       |     |                                                                              |
| 121 | [Best Time to But and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)                               | [Python](./python/problems/easy/best_time_to_buy_and_sell_stock.py)                  | _O(n)_                                                    | _O(1)_                                                                              | Easy       |     |                                                                              |
| 209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)                                           | [Python](./python/problems/medium/minimum_size_subarray_sum.py)                      | _O(n)_                                                    | _O(1)_                                                                              | Medium     |     |                                                                              |
| 239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)                                                 | [Python](./python/problems/hard/sliding_window_maximum.py)                           | _O(n)_, _n_ being the length of `nums`                    | _O(k)_, _k_ being the window size                                                   | Hard       |     |                                                                              |
| 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)               | [Python](./python/problems/medium/longest_repeating_character_replacement.py)        | _O(n)_                                                    | _O(1)_                                                                              | Medium     |     |                                                                              |
| 567 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/)                                                   | [Python](./python/problems/medium/permutation_in_string.py)                          | _O(n)_, _n_ being the length of s2                        | _O(k)_, _k_ being the length of s1                                                  | Medium     |     |                                                                              |

## Stack

| #   | Title                                                                                               | Solution                                                               | Time             | Space  | Difficulty | Tag | Note                            |
| --- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------- | ------ | ---------- | --- | ------------------------------- |
| 20  | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)                               | [Python](./python/problems/easy/valid_parentheses.py)                  | _O(n)_           | _O(n)_ | Easy       |     |                                 |
| 22  | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)                         | [Python](./python/problems/medium/generate_parentheses.py)             | _O(4^n/sqrt(n))_ | _O(n)_ | Medium     |     |                                 |
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [Python](./python/problems/medium/evaluate_reverse_polish_notation.py) | _O(n)_           | _O(n)_ | Medium     |     |                                 |
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/)                                               | [Python](./python/problems/medium/min_stack.py)                        | _O(1)_           | _O(1)_ | Medium     |     | Tuple in stack is interesting ! |

## Matrix

| #   | Title                                                       | Solution                                           | Time   | Space  | Difficulty | Tag | Note |
| --- | ----------------------------------------------------------- | -------------------------------------------------- | ------ | ------ | ---------- | --- | ---- |
| 36  | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | [Python](./python/problems/medium/valid_sudoku.py) | _O(1)_ | _O(1)_ | Medium     |     |      |

## Intervals

| #   | Title                                                           | Solution                                           | Time   | Space  | Difficulty | Tag | Note |
| --- | --------------------------------------------------------------- | -------------------------------------------------- | ------ | ------ | ---------- | --- | ---- |
| 228 | [Summary Ranges](https://leetcode.com/problems/summary-ranges/) | [Python](./python/problems/easy/summary_ranges.py) | _O(n)_ | _O(n)_ | Easy       |     |      |

## Linked-List

| #   | Title                                                                 | Solution                                              | Time   | Space  | Difficulty | Tag | Note |
| --- | --------------------------------------------------------------------- | ----------------------------------------------------- | ------ | ------ | ---------- | --- | ---- |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | [Python](./python/problems/easy/linked_list_cycle.py) | _O(n)_ | _O(1)_ | Easy       |     |      |

## Binary-Tree-General

| #   | Title                                                                                       | Solution                                                          | Time   | Space  | Difficulty | Tag | Note             |
| --- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------ | ------ | ---------- | --- | ---------------- |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Python](./python/problems/easy//maximum_depth_of_binary_tree.py) | _O(n)_ | _O(1)_ | Easy       | DFS | Use FIFO for BFS |

## Binary-Tree-BFS

| #   | Title                                                                                     | Solution                                                          | Time   | Space                                                  | Difficulty | Tag | Note |
| --- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------ | ------------------------------------------------------ | ---------- | --- | ---- |
| 199 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | [Python](./python/problems/medium/binary_tree_right_side_view.py) | _O(n)_ | _O(w)_ where w is the maximum width of the binary tree | Medium     |     |      |

## Binary-Search-Tree

| #   | Title                                                                                                   | Solution                                                               | Time   | Space  | Difficulty | Tag | Note               |
| --- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------ | ------ | ---------- | --- | ------------------ |
| 530 | [Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/) | [Python](./python/problems/easy/minimum_absolute_difference_in_bst.py) | _O(n)_ | _O(1)_ | Easy       |     | In-order traversal |

## Graph-General

| #   | Title                                                                 | Solution                                                | Time        | Space  | Difficulty | Tag | Note |
| --- | --------------------------------------------------------------------- | ------------------------------------------------------- | ----------- | ------ | ---------- | --- | ---- |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | [Python](./python/problems/medium/number_of_islands.py) | _O(n \* m)_ | _O(1)_ | Medium     |     |      |
