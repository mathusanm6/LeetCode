#include "test_add_two_numbers.h"

#include <cassert>
#include <iostream>
#include "../../../problems/easy/add_two_numbers/add_two_numbers.h"

void test_add_two_numbers() {
    assert(add_two_numbers(2, 3) == 5);
    assert(add_two_numbers(-1, 1) == 0);
    assert(add_two_numbers(0, 0) == 0);
    assert(add_two_numbers(100, 200) == 300);
    std::cout << "All tests passed!" << std::endl;
}

