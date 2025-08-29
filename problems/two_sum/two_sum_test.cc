#include "two_sum.h"

#include <gtest/gtest.h>
#include <vector>

struct TwoSumCase {
  const std::string test_name;
  const std::vector<int> nums;
  const int target;
  const std::vector<int> expected;
};

using TwoSumTest = ::testing::TestWithParam<TwoSumCase>;

TEST_P(TwoSumTest, TestCases) {
  const TwoSumCase &test_case = GetParam();
  const std::vector<int> result = twoSum(test_case.nums, test_case.target);
  EXPECT_EQ(result, test_case.expected);
}

INSTANTIATE_TEST_SUITE_P(
    TwoSumTestCases, TwoSumTest,
    ::testing::Values(TwoSumCase{.test_name = "BasicCase",
                                 .nums = {2, 7, 11, 15},
                                 .target = 9,
                                 .expected = {0, 1}},
                      TwoSumCase{.test_name = "MiddleElements",
                                 .nums = {3, 2, 4},
                                 .target = 6,
                                 .expected = {1, 2}},
                      TwoSumCase{.test_name = "DuplicateElements",
                                 .nums = {3, 3},
                                 .target = 6,
                                 .expected = {0, 1}},
                      TwoSumCase{.test_name = "NegativePositiveMix",
                                 .nums = {-3, 1, 2, 3},
                                 .target = 0,
                                 .expected = {0, 3}},
                      TwoSumCase{.test_name = "NoSolution",
                                 .nums = {0, 1},
                                 .target = -1,
                                 .expected = {-1, -1}},
                      TwoSumCase{.test_name = "TargetAtEnd",
                                 .nums = {1, 2, 3, 4, 5},
                                 .target = 8,
                                 .expected = {2, 4}},
                      TwoSumCase{.test_name = "LargeNumbers",
                                 .nums = {5, 75, 25},
                                 .target = 100,
                                 .expected = {1, 2}},
                      TwoSumCase{.test_name = "AllNegativeNumbers",
                                 .nums = {-1, -2, -3, -4, -5},
                                 .target = -8,
                                 .expected = {2, 4}},
                      TwoSumCase{.test_name = "DuplicateZeros",
                                 .nums = {0, 4, 3, 0},
                                 .target = 0,
                                 .expected = {0, 3}},
                      TwoSumCase{.test_name = "MultipleDuplicates",
                                 .nums = {1, 1, 1, 1},
                                 .target = 2,
                                 .expected = {0, 1}},
                      TwoSumCase{.test_name = "SingleElementNoSolution",
                                 .nums = {1},
                                 .target = 2,
                                 .expected = {-1, -1}},
                      TwoSumCase{.test_name = "TwoIdenticalElements",
                                 .nums = {2, 2},
                                 .target = 4,
                                 .expected = {0, 1}},
                      TwoSumCase{.test_name = "LargePositiveNegative",
                                 .nums = {1000, -1000},
                                 .target = 0,
                                 .expected = {0, 1}},
                      TwoSumCase{.test_name = "LargerArray",
                                 .nums = {1, 2, 3, 4, 5, 6},
                                 .target = 11,
                                 .expected = {4, 5}},
                      TwoSumCase{.test_name = "TwoZerosSumToZero",
                                 .nums = {0, 0},
                                 .target = 0,
                                 .expected = {0, 1}}),
    [](const ::testing::TestParamInfo<TwoSumCase> &info) {
      return info.param.test_name;
    });
