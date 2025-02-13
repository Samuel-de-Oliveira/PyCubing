from random import randint

def Cube2x2x2(size: int = 12, ANSI: bool = True) -> list:
  """
    This function generates a scramble for 2x2x2 Cube
    Following the WCA guidelines.
  """

  Moves_types: tuple = ('R', 'U', 'F')
  Orientation: tuple = ("", "'", "2")

  Moves = []
  for i in range(1, size + 1):
    Moves.append(
      Moves_types[randint(0, 2)] +
      Orientation[randint(0, 2)]
    )
  
  return Moves

if __name__ == "__main__":
  print("""
    This is a module file, then you should import it.
  """)
