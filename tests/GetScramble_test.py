import random
from PyCubing import GetScramble


def test_Cube3x3x3() -> None:
    """
    Test GetScramble.Cube3x3x3() function.
    """

    actual_output1: list = GetScramble.Cube3x3x3()
    actual_output2: list = GetScramble.Cube3x3x3()

    assert actual_output1 != actual_output2
