from enum import Enum
class Color(Enum):
    WHITE = 1
    BLACK = 2

    def __str__(self):
        if self is Color.WHITE:
            return 'W'
        else:
            return 'B'

    def __eq__(self, o):
        if self is o:
            return True
        else:
            return str(self) == o
