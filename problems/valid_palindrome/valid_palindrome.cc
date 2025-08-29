#include "valid_palindrome.h"

#include <algorithm>
#include <cctype>
#include <string>

bool isPalindrome(const std::string &str) {
    int left = 0;
    int right = static_cast<int>(str.size()) - 1;

    // Create a copy of the string and transform to lowercase
    std::string lowerStr = str;
    std::ranges::transform(lowerStr, lowerStr.begin(),
                           [](unsigned char character) { return std::tolower(character); });

    while (left < right) {
        // Move left pointer to the next alphanumeric character
        while (left < right && std::isalnum(lowerStr[left]) == 0) {
            ++left;
        }

        // Move right pointer to the previous alphanumeric character
        while (left < right && std::isalnum(lowerStr[right]) == 0) {
            --right;
        }

        // Compare characters at left and right pointers
        if (lowerStr[left] != lowerStr[right]) {
            return false;  // Not a palindrome
        }

        ++left;
        --right;
    }
    return true;  // Is a palindrome
}