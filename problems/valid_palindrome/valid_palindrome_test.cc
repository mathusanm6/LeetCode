#include "valid_palindrome.h"

#include <gtest/gtest.h>
#include <string>

struct ValidPalindromeCase {
    std::string test_name;
    std::string str;
    bool expected;
};

using ValidPalindromeTest = ::testing::TestWithParam<ValidPalindromeCase>;

TEST_P(ValidPalindromeTest, TestCases) {
    const ValidPalindromeCase &testCase = GetParam();
    const bool result = isPalindrome(testCase.str);
    EXPECT_EQ(result, testCase.expected);
}

INSTANTIATE_TEST_SUITE_P(
    ValidPalindromeTestCases, ValidPalindromeTest,
    ::testing::Values(
        ValidPalindromeCase{.test_name = "ClassicPanama",
                            .str = "A man, a plan, a canal: Panama",
                            .expected = true},
        ValidPalindromeCase{.test_name = "RaceCarFalse", .str = "race a car", .expected = false},
        ValidPalindromeCase{.test_name = "EmptyString", .str = "", .expected = true},
        ValidPalindromeCase{.test_name = "SingleChar", .str = "a", .expected = true},
        ValidPalindromeCase{.test_name = "CaseInsensitive", .str = "Aa", .expected = true},
        ValidPalindromeCase{.test_name = "TwoCharFalse", .str = "ab", .expected = false},
        ValidPalindromeCase{.test_name = "TwoCharTrue", .str = "aa", .expected = true},
        ValidPalindromeCase{.test_name = "SimplePalindrome", .str = "racecar", .expected = true},
        ValidPalindromeCase{.test_name = "SimpleFalse", .str = "hello", .expected = false},
        ValidPalindromeCase{.test_name = "SantaNasa", .str = "A Santa at NASA", .expected = true},
        ValidPalindromeCase{
            .test_name = "CarCatQuestion", .str = "Was it a car or a cat I saw?", .expected = true},
        ValidPalindromeCase{
            .test_name = "NixonApostrophe", .str = "No 'x' in Nixon", .expected = true},
        ValidPalindromeCase{.test_name = "MadamAdam", .str = "Madam, I'm Adam", .expected = true},
        ValidPalindromeCase{
            .test_name = "NeverOddEven", .str = "never odd or even", .expected = true},
        ValidPalindromeCase{.test_name = "NopeFalse", .str = "nope", .expected = false},
        ValidPalindromeCase{.test_name = "MixedAlphanumFalse", .str = "0P", .expected = false},
        ValidPalindromeCase{.test_name = "PanamaExclamation",
                            .str = "A man, a plan, a canal: Panama!",
                            .expected = true},
        ValidPalindromeCase{.test_name = "RaceEcarHyphen", .str = "race a E-car", .expected = true},
        ValidPalindromeCase{
            .test_name = "AbleElba", .str = "Able was I ere I saw Elba", .expected = true},
        ValidPalindromeCase{.test_name = "NumericPalindrome", .str = "12321", .expected = true},
        ValidPalindromeCase{.test_name = "NumericFalse", .str = "12345", .expected = false},
        ValidPalindromeCase{
            .test_name = "AlphanumPalindrome", .str = "a1b2c3c2b1a", .expected = true},
        ValidPalindromeCase{.test_name = "AlphanumFalse", .str = "1a2b3c3c2b1a", .expected = false},
        ValidPalindromeCase{
            .test_name = "OnlySpecialChars", .str = ".,!@#$%^&*()", .expected = true},
        ValidPalindromeCase{
            .test_name = "SpecialCharsMiddle", .str = "a.,!@#$%^&*()a", .expected = true},
        ValidPalindromeCase{.test_name = "DammitMad", .str = "Dammit, I'm mad!", .expected = true},
        ValidPalindromeCase{.test_name = "StepPets", .str = "Step on no pets", .expected = true},
        ValidPalindromeCase{
            .test_name = "RatQuestion", .str = "Was it a rat I saw?", .expected = true},
        ValidPalindromeCase{
            .test_name = "OwlWorm", .str = "Mr. Owl ate my metal worm", .expected = true}),
    [](const ::testing::TestParamInfo<ValidPalindromeCase> &info) { return info.param.test_name; });