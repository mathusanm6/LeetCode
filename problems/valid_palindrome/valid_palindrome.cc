#include "valid_palindrome.h"

#include <algorithm>

using std::string;

bool isPalindrome(string s) {
  int left = 0;
  int right = static_cast<int>(s.size()) - 1;

  // Transform the string (in-place) to lowercase
  std::transform(s.begin(), s.end(), s.begin(),
                 [](unsigned char c) { return std::tolower(c); });

  while (left < right) {
    // Move left pointer to the next alphanumeric character
    while (left < right && !std::isalnum(s[left])) {
      ++left;
    }

    // Move right pointer to the previous alphanumeric character
    while (left < right && !std::isalnum(s[right])) {
      --right;
    }

    // Compare characters at left and right pointers
    if (s[left] != s[right]) {
      return false; // Not a palindrome
    }

    ++left;
    --right;
  }
  return true; // Is a palindrome
}