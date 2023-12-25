from problems.medium.snakes_and_ladders import Solution

def test_snakes_and_ladders():

    solution = Solution

    # Test Case 1
    board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    assert solution.snakesAndLadders(solution, board) == 4

    # Test Case 2
    board = [[-1,-1],[-1,3]]
    assert solution.snakesAndLadders(solution, board) == 1