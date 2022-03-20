from typing import List
from collections import defaultdict

from tikz_elements.NodeStyle import NodeStyle
from tikz_elements.TikzCoord import TikzCoord


class TikzNode:

    style: NodeStyle
    params: dict[str,str]
    name: str = ""
    label: str = ""
    location: TikzCoord = None

    def __init__(self, style: NodeStyle, name: str, params: List[List[str]] = [], location: TikzCoord = None):
        self.style = style
        self.name = name
        self.location = location

        self.params = defaultdict()
        if params:
            for keyword, value in params:
                self.params[keyword] = value

    def params_to_string(self) -> str:
        ret: str = ""

        for keyword, value in self.params.items():
            ret += f", {keyword}={value}"

        return ret

    def path_id(self):
        return self.name

    def tikz_code(self) -> str:
        tikz_code: str = f"\t\\node[{self.style}"

        if self.params:
            tikz_code += f"{self.params_to_string()}"

        tikz_code += "]"

        if self.name:
            tikz_code += f" ({self.name})"

        if self.location != None:
            tikz_code += f" at {self.location.x,self.location.y}"

        tikz_code += " {"

        if self.label:
            tikz_code += f" \u007b{self.label}\u007d"

        tikz_code += "};"

        return tikz_code