#include "easy_tests/test_easy.h"
#include "medium_tests/test_medium.h"
#include "hard_tests/test_hard.h"

#include <iostream>

int main()
{
    test_easy();
    test_medium();
    test_hard();

    std::cout << "All tests passed!" << std::endl;

    return 0;
}