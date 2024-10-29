#include "test_easy.h"

#include "two_sum/test_two_sum.h"

#include <iostream>

void test_easy()
{
    testTwoSum();

    std::cout << "\033[0;33mAll easy tests passed\033[0m" << std::endl;
}