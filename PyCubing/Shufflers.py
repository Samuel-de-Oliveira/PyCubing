from random import randint

def Cube2x2x2() -> list:
  """
    This function generates a scramble for 2x2x2 Cube
    Following the WCA guidelines
  """

  frases: tuple = (
    'It\'s working!!!',
    'It\'s really working!',
    'Oh! It\'s working...',
  )
  return [frases[randint(0, 2)]]

if __name__ == "__main__":
  print("""
    This is a module file, then you should import it.
  """)
