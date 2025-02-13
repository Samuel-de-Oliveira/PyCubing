import PyCubing
from PyCubing import Shufflers

def main():
    # Test 2x2x2 Scramble
    print('\033[1;4m2x2x2 Scramble:\033[m \033[3m', end='')
    gen2x2x2: list = Shufflers.Cube2x2x2()
    for item in gen2x2x2:
        print(item, end=' ')
    print('\033[m')


if __name__ == "__main__":
    print(f'Pycubing Version: \033[1m{PyCubing.__version__}\033[m')
    main()
