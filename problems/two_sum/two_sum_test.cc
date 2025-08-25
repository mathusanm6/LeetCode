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

TEST_F(TwoSumTest, TestCases)
{
    const TwoSumCase &test_case = GetParam();
    const vector<int> result = twoSum(test_case.nums, test_case.target);
    EXPECT_EQ(result, test_case.expected);
}

INSTANTIATE_TEST_SUITE_P(
    TwoSumTestCases, TwoSumTest,
    ::testing::Values(
        TwoSumCase{{2, 7, 11, 15}, 9, {0, 1}},
        TwoSumCase{{3, 2, 4}, 6, {1, 2}},
        TwoSumCase{{3, 3}, 6, {0, 1}},
        TwoSumCase{{-3, 1, 2, 3}, 0, {0, 3}},
        TwoSumCase{{0, 1}, -1, {-1, -1}} // Edge case: no solution
        ));
