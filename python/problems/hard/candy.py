from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        def slope(i):
            if i < 0 or i >= n:
                return None

            if ratings[i] > ratings[i + 1]:
                return -1
            elif ratings[i] < ratings[i + 1]:
                return 1
            else:
                return 0

        n = len(ratings)

        steep_arr = [slope(i) for i in range(n - 1)]

        candies = [1] * n

        for l in range(n - 1):
            if steep_arr[l] == 1 and candies[l + 1] <= candies[l]:
                candies[l + 1] = candies[l] + 1

        for r in range(n - 1, 0, -1):
            if steep_arr[r - 1] == -1 and candies[r] >= candies[r - 1]:
                candies[r - 1] = candies[r] + 1

        return sum(candies)
