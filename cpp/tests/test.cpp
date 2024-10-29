#include "easy_tests/test_easy.h"
#include "medium_tests/test_medium.h"
#include "hard_tests/test_hard.h"

#include <iostream>

int main()
{
    test_easy();
    test_medium();
    test_hard();

    std::cout << "\033[1;32m[All tests passed]\033[0m" << std::endl;
    return 0;
}