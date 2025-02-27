import PyCubing
from PyCubing import GetScramble


def Test_Scrambles():
    # Test 2x2x2 Scramble
    print("\033[1;4m2x2x2's Scramble:\033[m \033[3m", end='')
    gen2x2x2: list = GetScramble.Cube2x2x2()
    for item in gen2x2x2:
        print(item, end=' ')
    print('\033[m')

    # Test 3x3x3 Scramble
    print("\033[1;4m3x3x3's Scramble:\033[m \033[3m", end='')
    gen3x3x3: list = GetScramble.Cube3x3x3()
    for item in gen3x3x3:
        print(item, end=' ')
    print('\033[m')

    # Test 4x4x4 Scramble
    print("\033[1;4m4x4x4's Scramble:\033[m \033[3m", end='')
    gen4x4x4: list = GetScramble.Cube4x4x4()
    for item in gen4x4x4:
        print(item, end=' ')
    print('\033[m')

    # Test 5x5x5 Scramble
    print("\033[1;4m5x5x5's Scramble:\033[m \033[3m", end='')
    gen5x5x5: list = GetScramble.Cube5x5x5()
    for item in gen5x5x5:
        print(item, end=' ')
    print('\033[m')

    # Test 6x6x6 Scramble
    print("\033[1;4m6x6x6's Scramble:\033[m \033[3m", end='')
    gen6x6x6: list = GetScramble.Cube6x6x6()
    for item in gen6x6x6:
        print(item, end=' ')
    print('\033[m')

    # Test 7x7x7 Scramble
    print("\033[1;4m7x7x7's Scramble:\033[m \033[3m", end='')
    gen7x7x7: list = GetScramble.Cube7x7x7()
    for item in gen7x7x7:
        print(item, end=' ')
    print('\033[m')

    # Test Pyraminx Scramble
    print("\033[1;4mPyraminx's Scramble:\033[m \033[3m", end='')
    genPyra: list = GetScramble.Pyraminx()
    for item in genPyra:
        print(item, end=' ')
    print('\033[m')

    # Test Skewb Scramble
    print("\033[1;4mSkewb's Scramble:\033[m \033[3m", end='')
    genSkewb: list = GetScramble.Skewb()
    for item in genSkewb:
        print(item, end=' ')
    print('\033[m')

    # Test Square One Scramble
    print("\033[1;4mSquare One's Scramble:\033[m \033[3m", end='')
    genSquareOne: list = GetScramble.Square_One()
    for item in genSquareOne:
        print(item, end=' ')
    print('\033[m')

    print('-' * 25)


def test_API() -> None:
    print('Top 10 WCA 3x3x3 average records')

    ranking: dict = PyCubing.get_wca_ranking()
    for rank in ranking:
        print(f'\033[1m{rank}:\033[m {ranking[rank]}')

    print('-' * 25)


if __name__ == '__main__':
    print(f'Pycubing Version: \033[1m{PyCubing.__version__}\033[m')
    Test_Scrambles()
    test_API()
