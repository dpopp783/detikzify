from typing import List

class NodeType:

    name: str
    params: List[List[str]] = [[]]
    shape: str = ""


    def __init__(self, name:str, shape:str, params: List[List[str]]):
        self.name = name
        self.shape = shape
        self.params = params

    def __repr__(self):
        return self.name

    def params_to_string(self) -> str:

        ret: str = ""

        for param in self.params:
            if len(param) == 1:
                ret += f", {param[0]}"
            elif len(param) > 1:
                ret += f", {param[0]}={param[1]}"

        return ret

    def tikz_code(self) -> str:
        tikz_code: str = f"\t\\tikzstyle\u007b{self.name}\u007d = [draw"

        if self.shape:
            tikz_code += f", {self.shape}"

        if self.params[0]:
            tikz_code += f", {self.params_to_string()}]"

        tikz_code += "]"

        return tikz_code
