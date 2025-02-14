import PyCubing
from PyCubing import GetScramble


def main():
    # Test 2x2x2 Scramble
    print('\033[1;4m2x2x2 Scramble:\033[m \033[3m', end='')
    gen2x2x2: list = GetScramble.Cube2x2x2()
    for item in gen2x2x2:
        print(item, end=' ')
    print('\033[m')

    # Test 3x3x3 Scramble
    print('\033[1;4m3x3x3 Scramble:\033[m \033[3m', end='')
    gen3x3x3: list = GetScramble.Cube3x3x3()
    for item in gen3x3x3:
        print(item, end=' ')
    print('\033[m')

    # Test 4x4x4 Scramble
    print('\033[1;4m4x4x4 Scramble:\033[m \033[3m', end='')
    gen4x4x4: list = GetScramble.Cube4x4x4()
    for item in gen4x4x4:
        print(item, end=' ')
    print('\033[m')


if __name__ == "__main__":
    print(f'Pycubing Version: \033[1m{PyCubing.__version__}\033[m')
    main()
