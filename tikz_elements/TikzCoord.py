from dataclasses import dataclass
from dataclasses import field

@dataclass
class TikzCoord:
    """Class for keeping track of points x and y"""
    x: float = field()
    y: float = field()
    name: str = field(init=False)

    def path_id(self):
        return f"{self.x,self.y}"
