from ransom_note import Solution

def test_ransom_note():
    solution = Solution

    # Test Case 1
    ransomNote = "a"
    magazine = "b"
    assert solution.canConstruct(solution, ransomNote, magazine) == False

    # Test Case 2
    ransomNote = "aa"
    magazine = "ab"
    assert solution.canConstruct(solution, ransomNote, magazine) == False

    # Test Case 3
    ransomNote = "aa"
    magazine = "aab"
    assert solution.canConstruct(solution, ransomNote, magazine) == True

    # Test Case 4
    ransomNote = "fffbfg"
    magazine = "effjfggbffjdgbjjhhdegh"
    assert solution.canConstruct(solution, ransomNote, magazine) == True

    # Test Case 5
    ransomNote = ""
    magazine = ""
    assert solution.canConstruct(solution, ransomNote, magazine) == True