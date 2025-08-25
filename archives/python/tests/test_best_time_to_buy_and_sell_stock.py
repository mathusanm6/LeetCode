from problems.easy.best_time_to_buy_and_sell_stock import Solution

solution = Solution()


def test_sample_one():
    prices = [7, 1, 5, 3, 6, 4]
    assert solution.maxProfit(prices) == 5


def test_sample_two():
    prices = [7, 6, 4, 3, 1]
    assert solution.maxProfit(prices) == 0
