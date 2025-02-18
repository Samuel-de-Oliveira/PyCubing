# PyCubing
A Python module to make speedcubing projects a piece of cake.

## How to install
```sh
pip install PyCubing
```

> ⚠️ Note: PiPy is not working for this project yet!!!

## Usage
This code generate a scramble for a 2x2x2 cube:
```python
from PyCubing import GetScramble

if __name__ == "__main__":
  scramble: list = GetScramble.Cube2x2x2()
  print(f'A 2x2x2 Scramble: {scramble}')
```

#### Made in Brazil :brazil:
