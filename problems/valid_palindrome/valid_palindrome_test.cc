#include "valid_palindrome.h"

#include <gtest/gtest.h>
#include <string>

using std::string;

struct ValidPalindromeCase {
  const std::string test_name;
  const string s;
  const bool expected;
};

using ValidPalindromeTest = ::testing::TestWithParam<ValidPalindromeCase>;

TEST_P(ValidPalindromeTest, TestCases) {
  const ValidPalindromeCase &test_case = GetParam();
  const bool result = isPalindrome(test_case.s);
  EXPECT_EQ(result, test_case.expected);
}

INSTANTIATE_TEST_SUITE_P(
    ValidPalindromeTestCases, ValidPalindromeTest,
    ::testing::Values(
        ValidPalindromeCase{.test_name = "ClassicPanama",
                            .s = "A man, a plan, a canal: Panama",
                            .expected = true},
        ValidPalindromeCase{
            .test_name = "RaceCarFalse", .s = "race a car", .expected = false},
        ValidPalindromeCase{
            .test_name = "EmptyString", .s = "", .expected = true},
        ValidPalindromeCase{
            .test_name = "SingleChar", .s = "a", .expected = true},
        ValidPalindromeCase{
            .test_name = "CaseInsensitive", .s = "Aa", .expected = true},
        ValidPalindromeCase{
            .test_name = "TwoCharFalse", .s = "ab", .expected = false},
        ValidPalindromeCase{
            .test_name = "TwoCharTrue", .s = "aa", .expected = true},
        ValidPalindromeCase{
            .test_name = "SimplePalindrome", .s = "racecar", .expected = true},
        ValidPalindromeCase{
            .test_name = "SimpleFalse", .s = "hello", .expected = false},
        ValidPalindromeCase{
            .test_name = "SantaNasa", .s = "A Santa at NASA", .expected = true},
        ValidPalindromeCase{.test_name = "CarCatQuestion",
                            .s = "Was it a car or a cat I saw?",
                            .expected = true},
        ValidPalindromeCase{.test_name = "NixonApostrophe",
                            .s = "No 'x' in Nixon",
                            .expected = true},
        ValidPalindromeCase{
            .test_name = "MadamAdam", .s = "Madam, I'm Adam", .expected = true},
        ValidPalindromeCase{.test_name = "NeverOddEven",
                            .s = "never odd or even",
                            .expected = true},
        ValidPalindromeCase{
            .test_name = "NopeFalse", .s = "nope", .expected = false},
        ValidPalindromeCase{
            .test_name = "MixedAlphanumFalse", .s = "0P", .expected = false},
        ValidPalindromeCase{.test_name = "PanamaExclamation",
                            .s = "A man, a plan, a canal: Panama!",
                            .expected = true},
        ValidPalindromeCase{.test_name = "RaceEcarHyphen",
                            .s = "race a E-car",
                            .expected = true},
        ValidPalindromeCase{.test_name = "AbleElba",
                            .s = "Able was I ere I saw Elba",
                            .expected = true},
        ValidPalindromeCase{
            .test_name = "NumericPalindrome", .s = "12321", .expected = true},
        ValidPalindromeCase{
            .test_name = "NumericFalse", .s = "12345", .expected = false},
        ValidPalindromeCase{.test_name = "AlphanumPalindrome",
                            .s = "a1b2c3c2b1a",
                            .expected = true},
        ValidPalindromeCase{.test_name = "AlphanumFalse",
                            .s = "1a2b3c3c2b1a",
                            .expected = false},
        ValidPalindromeCase{.test_name = "OnlySpecialChars",
                            .s = ".,!@#$%^&*()",
                            .expected = true},
        ValidPalindromeCase{.test_name = "SpecialCharsMiddle",
                            .s = "a.,!@#$%^&*()a",
                            .expected = true},
        ValidPalindromeCase{.test_name = "DammitMad",
                            .s = "Dammit, I'm mad!",
                            .expected = true},
        ValidPalindromeCase{
            .test_name = "StepPets", .s = "Step on no pets", .expected = true},
        ValidPalindromeCase{.test_name = "RatQuestion",
                            .s = "Was it a rat I saw?",
                            .expected = true},
        ValidPalindromeCase{.test_name = "OwlWorm",
                            .s = "Mr. Owl ate my metal worm",
                            .expected = true}),
    [](const ::testing::TestParamInfo<ValidPalindromeCase> &info) {
      return info.param.test_name;
    });