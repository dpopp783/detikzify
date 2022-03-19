from typing import List
import Point

class TikzNode:

    node_type: str
    params: dict[str,str]
    label: str
    location: Point

    def __init__(self, nt: str, *params: List[List[str]]):
        self.node_type = nt

        self.params = dict()
        for keyword, value in params:
            params[keyword] = value

    def params_to_string(self) -> str:
        ret: str = ""

        for keyword, value in self.params.items():
            ret += f", {keyword}={value}"

        return ret[2:]

    def tikz_code(self) -> str:
        tikz_code: str = f"\\node[{self.node_type}, {self.params_to_string()}]"

        if self.location != None:
            tikz_code += f" at ({self.location.x,self.location.y})"

        if self.label:
            tikz_code += f" \u007b{self.label}\u007d"

        tikz_code += ";"

        return tikz_code