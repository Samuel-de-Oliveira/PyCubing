import PyCubing
from PyCubing import Shufflers

def main():
    gen2x2x2: list = Shufflers.Cube2x2x2()
    for item in gen2x2x2:
        print(item)


if __name__ == "__main__":
    print(f'Pycubing Version: \033[1m{PyCubing.__version__}\033[m')
    main()
