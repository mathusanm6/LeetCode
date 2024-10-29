#include "test_two_sum.h"

#include <cassert>
#include <iostream>
#include "../../../problems/easy/two_sum/two_sum.h"

void test_one()
{
    std::vector<int> input = {2, 7, 11, 15};
    std::vector<int> expected = {0, 1};
    assert(twoSum(input, 9) == expected);
}

void test_two()
{
    std::vector<int> input = {3, 2, 4};
    std::vector<int> expected = {1, 2};
    assert(twoSum(input, 6) == expected);
}

void test_three()
{
    std::vector<int> input = {3, 3};
    std::vector<int> expected = {0, 1};
    assert(twoSum(input, 6) == expected);
}

void testTwoSum()
{
    test_one();
    test_two();
    test_three();

    std::cout << "Two sum tests passed" << std::endl;
}