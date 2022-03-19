from tikz_elements.TikzNode import TikzNode
from tikz_elements.Point import Point
from typing import List

class Line:

    start = None
    out_arrow: str = ""
    in_arrow: str = ""
    params: List[str] = []

    def __init__(self, start, end, **kwargs):

        self.start = start
        self.end = end

        if "from_arrow" in kwargs.keys():
            self.out_arrow = "<" if kwargs["from_arrow"] else ""

        if "to_arrow" in kwargs.keys():
            self.in_arrow = ">" if kwargs["to_arrow"] else ""

        if "bend" in kwargs.keys():
            bend = kwargs["bend"].lower()
            if bend in ["r","right"]:
                self.params.append("bend right")
            elif bend in ["l", "left"]:
                self.params.append("bend left")

    def params_to_string(self) -> str:
        return ", ".join(self.params)

    def tikz_code(self):
        code = f"\t\draw[{self.out_arrow}-{self.in_arrow}] ({self.start.path_id()}) to "

        if self.params:
            code += f"[{self.params_to_string()}] "

        code += f"({self.end.path_id()});"
        return code