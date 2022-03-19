from tikz_elements.TikzNode import TikzNode
from tikz_elements.Point import Point
from typing import List

class Line:

    start = None
    end = None
    out_arrow: str = ""
    in_arrow: str = ""

    def __init__(self, start, end, arrow_flags: List[bool]):

        self.start = start
        self.end = end
        self.out_arrow = "<" if arrow_flags[0] else ""
        self.in_arrow = ">" if arrow_flags[1] else ""

    def tikz_code(self):
        code = f"\t\draw[{self.out_arrow}-{self.in_arrow}] ({self.start.path_id()}) -- ({self.end.path_id()});"
        return code