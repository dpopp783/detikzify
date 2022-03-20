from typing import List

class NodeType:

    name: str
    params: List[str] = []
    shape: str
    min_size: float


    def __init__(self, name: str, min_size: float, shape: str, **kwargs):
        self.name = name
        self.params.append("draw")
        self.params.append(shape)
        self.shape = shape
        self.min_size = min_size
        self.params.append(f"minimum size={self.min_size} cm")

        for kw, val in kwargs.items():
            self.params.append(f"{kw}={val}")

    def __repr__(self):
        return self.name

    def params_to_string(self) -> str:
        return ", ".join(self.params)

    def tikz_code(self) -> str:
        tikz_code: str = f"\t\\tikzstyle\u007b{self.name}\u007d = [{self.params_to_string()}]"

        return tikz_code

