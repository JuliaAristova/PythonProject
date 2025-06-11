from typing import Final

name: str = 'Bob'
age: int = 20
weight: float = 160.5
print(type(weight))

weight = 161
print(type(weight))

# constants - naming convention - capital
VERSION: Final[str] = '1.0.12'

VERSION = '1.0.13'          #warning it is Final, but you can change it
print(VERSION)
