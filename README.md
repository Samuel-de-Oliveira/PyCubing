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
from PyCubing import Shufflers

if __name__ == "__main__":
  scramble: list = Shufflers.Cube2x2x2()
  print(f'A 2x2x2 Scramble: {scramble}')
```

#### Made in Brazil :brazil:
