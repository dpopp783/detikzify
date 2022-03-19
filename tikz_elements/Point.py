from dataclasses import dataclass
from dataclasses import field

@dataclass
class Point:
    """Class for keeping track of points x and y"""
    x: int = field()
    y: int = field()
    name: str = field(init=False)

    def path_id(self):
        return f"{self.x,self.y}"
