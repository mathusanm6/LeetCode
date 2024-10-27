from problems.easy.valid_anagram import Solution

solution = Solution()


def test_anagram():
    s = "anagram"
    t = "nagaram"
    assert solution.isAnagram(s, t)


def test_not_anagram():
    s = "rat"
    t = "car"
    assert not solution.isAnagram(s, t)


def test_empty_strings():
    s = ""
    t = ""
    assert solution.isAnagram(s, t)


def test_one_empty_string():
    s = ""
    t = "a"
    assert not solution.isAnagram(s, t)
