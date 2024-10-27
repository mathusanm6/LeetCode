from problems.hard.trapping_rain_water_o_n import Solution as trap_o_n
from problems.hard.trapping_rain_water_o_1 import Solution as trap_o_1


def test_trapping_rain_water():

    # Test Case 1
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert trap_o_n().trap(height) == 6
    assert trap_o_1().trap(height) == 6

    # Test Case 2
    height = [4, 2, 0, 3, 2, 5]
    assert trap_o_n().trap(height) == 9
    assert trap_o_1().trap(height) == 9

    # Test Case 3
    height = [4, 2, 3]
    assert trap_o_n().trap(height) == 1
    assert trap_o_1().trap(height) == 1

    # Test Case 4
    height = [4, 2, 3, 1]
    assert trap_o_n().trap(height) == 1
    assert trap_o_1().trap(height) == 1
