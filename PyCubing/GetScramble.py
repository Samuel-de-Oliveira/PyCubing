from random import randint

__all__: list = [
    'Cube2x2x2',
    'Cube3x3x3',
    'Cube4x4x4',
    'Pyraminx',
]


def sameAxis(MoveA: str, MoveB: str, MoveC: str) -> bool:
    """
    Internal function to check if a group of 3 movements
    are from the same axis.
    A sequence of 3 moves in the same aixis is not valid.
    Ex.: R L R, F B F, U D U, L R L, etc.
    """
    concatened: str = MoveA[-1] + MoveB[-1] + MoveC[-1]
    return concatened == 'xxx' or concatened == 'yyy' or concatened == 'zzz'


def Cube2x2x2(size: int = 10) -> list:
    """
    This function generates a scramble for 2x2x2 Cube
    Following the WCA guidelines.
    """

    Moves_types: tuple = ('R', 'U', 'F')
    Orientation: tuple = ('', "'", '2')

    MoveA: str = ''
    Moves: list = []

    for move in range(1, size + randint(0, 3)):
        while True:
            MoveB: str = Moves_types[randint(0, len(Moves_types) - 1)]
            if MoveB != MoveA:
                break

        MoveA: str = MoveB
        Moves.append(MoveB + Orientation[randint(0, len(Orientation) - 1)])

    return Moves


def Cube3x3x3(size: int = 21) -> list:
    """
    This function generates a scramble for 3x3x3 Cube
    Following the WCA guidelines.
    """

    Moves_Types: tuple = ('Rx', 'Uy', 'Bz', 'Lx', 'Dy', 'Fz')
    Orientation: tuple = ('', "'", '2')

    MoveA: str = ' '
    MoveB: str = ' '
    Moves: list = []

    for move in range(1, size + randint(0, 5)):
        while True:
            MoveC: str = Moves_Types[randint(0, len(Moves_Types) - 1)]
            if not sameAxis(MoveA, MoveB, MoveC) and MoveC != MoveB:
                break

        MoveA: str = MoveB
        MoveB: str = MoveC
        Moves.append(MoveC[0] + Orientation[randint(0, len(Orientation) - 1)])

    return Moves


def Cube4x4x4(size: int = 40) -> list:
    """
    This function generates a scramble for 4x4x4 Cube
    Following the WCA guidelines.
    """

    Moves_Types: tuple = ('Rx', 'Uy', 'Bz', 'Lx', 'Dy', 'Fz')
    Orientation: tuple = ('', "'", '2', 'w', "w'", 'w2')

    MoveA: str = ' '
    MoveB: str = ' '
    Moves: list = []

    for move in range(1, size + randint(0, 5)):
        while True:
            MoveC: str = Moves_Types[randint(0, len(Moves_Types) - 1)]
            if not sameAxis(MoveA, MoveB, MoveC) and MoveC != MoveB:
                break

        MoveA: str = MoveB
        MoveB: str = MoveC
        Moves.append(MoveC[0] + Orientation[randint(0, len(Orientation) - 1)])

    return Moves


def Cube5x5x5(size: int = 55) -> list:
    """
    This function generates a scramble for 4x4x4 Cube
    Following the WCA guidelines.
    """

    Moves_Types: tuple = ('Rx', 'Uy', 'Bz', 'Lx', 'Dy', 'Fz')
    Orientation: tuple = ('', "'", '2', 'w', "w'", 'w2')

    MoveA: str = ' '
    MoveB: str = ' '
    Moves: list = []

    for move in range(0, size + randint(0, 5)):
        while True:
            MoveC: str = Moves_Types[randint(0, len(Moves_Types) - 1)]
            if not sameAxis(MoveA, MoveB, MoveC) and MoveC != MoveB:
                break

        MoveA: str = MoveB
        MoveB: str = MoveC
        Moves.append(MoveC[0] + Orientation[randint(0, len(Orientation) - 1)])

    return Moves


def Pyraminx(edges_size: int = 9, corner_sizes: int = 3):
    """
    This function generates a scramble for Pyraminx
    Following the WCA guidelines.
    """

    Moves_Types: tuple = ('R', 'L', 'U', 'B')
    Orientation: tuple = ('', "'")

    Moves: list = []

    # Edges moves
    MoveA: str = ''
    for move in range(1, edges_size + randint(0, 1)):
        while True:
            MoveB: str = Moves_Types[randint(0, len(Moves_Types) - 1)]
            if MoveB != MoveA:
                break

        MoveA: str = MoveB
        Moves.append(MoveB + Orientation[randint(0, len(Orientation) - 1)])

    MoveA: str = ''
    for move in range(1, corner_sizes + randint(0, 1)):
        while True:
            MoveB: str = Moves_Types[randint(0, len(Moves_Types) - 1)].lower()
            if MoveB != MoveA:
                break

        MoveA: str = MoveB
        Moves.append(MoveB + Orientation[randint(0, len(Orientation) - 1)])

    return Moves


def Skewb(size: int = 9) -> list:
    """
    This function generates a scramble for Skewb
    Following the WCA guidelines.
    """

    Moves_Types: tuple = ('R', 'L', 'U', 'B')
    Orientation: tuple = ('', "'")

    MoveA: str = ''
    Moves: list = []
    for move in range(1, size + randint(0, 1)):
        while True:
            MoveB: str = Moves_Types[randint(0, len(Moves_Types) - 1)]
            if MoveB != MoveA:
                break

        MoveA: str = MoveB
        Moves.append(MoveB + Orientation[randint(0, len(Orientation) - 1)])

    return Moves


if __name__ == '__main__':
    print('This is a module file, then you should import it.')
