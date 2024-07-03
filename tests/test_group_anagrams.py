from helpers.list import equal_ignore_order
from problems.medium.group_anagrams import Solution

solution = Solution()


def test_sample_one():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    # To avoid unexpected order issue...
    unordered_ans = solution.groupAnagrams(strs)
    ordered_ans = []
    for li in unordered_ans:
        ordered_ans.append(sorted(li))

    assert equal_ignore_order(ordered_ans, expected)


def test_sample_two():
    strs = [""]
    expected = [[""]]
    assert equal_ignore_order(solution.groupAnagrams(strs), expected)


def test_sample_three():
    strs = ["a"]
    expected = [["a"]]
    assert equal_ignore_order(solution.groupAnagrams(strs), expected)
