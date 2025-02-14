from random import randint

__all__: list = [
  'Cube2x2x2',
  'Cube3x3x3',
]


def sameAxis(MoveA: str, MoveB: str, MoveC: str) -> None:
    """
      Internal function to check if a group of 3 movements
      are from the same axis.
      A sequence of 3 moves in the same aixis is not valid.
      Ex.: R L R, F B F, U D U, L R L, etc.
    """
    concatened: str = MoveA[-1] + MoveB[-1] + MoveC[-1]
    return concatened == "xxx" or concatened == "yyy" or concatened == "zzz"


def Cube2x2x2(size: int = 12) -> list:
  """
    This function generates a scramble for 2x2x2 Cube
    Following the WCA guidelines.
  """

  Moves_types: tuple = ('R', 'U', 'F')
  Orientation: tuple = ("", "'", "2")

  MoveA: str   = ''
  Moves: list  = []

  for i in range(1, size + 1):
    while True:
      MoveB: str = Moves_types[randint(0, len(Moves_types) - 1)]
      if MoveB != MoveA:
        break

    MoveA: str = MoveB
    Moves.append(MoveB + Orientation[randint(0, len(Orientation) - 1)])
  
  return Moves


def Cube3x3x3(size: int = 16) -> list:
  """
    This function generates a scramble for 3x3x3 Cube
    Following the WCA guidelines.
  """

  Moves_Types: tuple = ('Rx', 'Uy', 'Bz', 'Lx', 'Dy', 'Fz')
  Orientation: tuple = ("", "'", "2")

  MoveA: str  = ' '
  MoveB: str  = ' '
  Moves: list = []

  for i in range(1, size + 1):
    while True:
      MoveC: str = Moves_Types[randint(0, len(Moves_Types) - 1)]
      if (not sameAxis(MoveA, MoveB, MoveC) and MoveC != MoveB): break
  
    MoveB: str = MoveC
    MoveA: str = MoveB
    Moves.append(MoveC[0] + Orientation[randint(0, len(Orientation) - 1)])

  return Moves


if __name__ == "__main__":
  print("""
    This is a module file, then you should import it.
  """)
