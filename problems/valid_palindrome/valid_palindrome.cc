#include "valid_palindrome.h"

#include <algorithm>
#include <cctype>

bool isPalindrome(const std::string &s) {
  int left = 0;
  int right = static_cast<int>(s.size()) - 1;

  // Create a copy of the string and transform to lowercase
  std::string s_lower = s;
  std::transform(s_lower.begin(), s_lower.end(), s_lower.begin(),
                 [](unsigned char c) { return std::tolower(c); });

  while (left < right) {
    // Move left pointer to the next alphanumeric character
    while (left < right && !std::isalnum(s_lower[left])) {
      ++left;
    }

    // Move right pointer to the previous alphanumeric character
    while (left < right && !std::isalnum(s_lower[right])) {
      --right;
    }

    // Compare characters at left and right pointers
    if (s_lower[left] != s_lower[right]) {
      return false; // Not a palindrome
    }

    ++left;
    --right;
  }
  return true; // Is a palindrome
}