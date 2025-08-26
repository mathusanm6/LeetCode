#include "two_sum.h"

#include <gtest/gtest.h>
#include <vector>

using std::vector;

struct TwoSumCase
{
    const vector<int> nums;
    const int target;
    const vector<int> expected;
};

using TwoSumTest = ::testing::TestWithParam<TwoSumCase>;

TEST_P(TwoSumTest, TestCases)
{
    const TwoSumCase &test_case = GetParam();
    const vector<int> result = twoSum(test_case.nums, test_case.target);
    EXPECT_EQ(result, test_case.expected);
}

INSTANTIATE_TEST_SUITE_P(
    TwoSumTestCases, TwoSumTest,
    ::testing::Values(
        TwoSumCase{{2, 7, 11, 15}, 9, {0, 1}},        // Basic case
        TwoSumCase{{3, 2, 4}, 6, {1, 2}},             // Middle elements
        TwoSumCase{{3, 3}, 6, {0, 1}},                // Duplicate elements
        TwoSumCase{{-3, 1, 2, 3}, 0, {0, 3}},         // Negative and positive mix
        TwoSumCase{{0, 1}, -1, {-1, -1}},             // Edge case: no solution
        TwoSumCase{{1, 2, 3, 4, 5}, 8, {2, 4}},       // Target at end
        TwoSumCase{{5, 75, 25}, 100, {1, 2}},         // Large numbers
        TwoSumCase{{-1, -2, -3, -4, -5}, -8, {2, 4}}, // All negative numbers
        TwoSumCase{{0, 4, 3, 0}, 0, {0, 3}},          // Duplicate zeros
        TwoSumCase{{1, 1, 1, 1}, 2, {0, 1}},          // Multiple duplicates
        TwoSumCase{{1}, 2, {-1, -1}},                 // Single element, no solution
        TwoSumCase{{2, 2}, 4, {0, 1}},                // Two identical elements that sum to target
        TwoSumCase{{1000, -1000}, 0, {0, 1}},         // Large positive and negative
        TwoSumCase{{1, 2, 3, 4, 5, 6}, 11, {4, 5}},   // Larger array
        TwoSumCase{{0, 0}, 0, {0, 1}}                 // Two zeros sum to zero
        ));
